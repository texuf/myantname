
from app import app
from flask import json, jsonify, redirect, request
from scripts.levenshtein import levenshtein3
import urllib2

response_data = None


@app.route('/<myname>')
@app.route('/<myname>/')
def myname(myname):
    global response_data
    
    if response_data is None:

        url = "http://www.antweb.org/api/?rank=species"
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        
        response_data = json.loads(response.read())

    for rd in response_data:
        rd['l2'] = levenshtein3(myname.lower(),rd['species'].lower())

    response_data.sort(key=lambda x:x['l2'], reverse=False)


    ret_val = []
    for r in response_data[0:10]:
        url = "http://www.antweb.org/api/?rank=species&name=%s" % r['species']
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        spec = {'name':r['species']}
        spec['specimens'] = len(json.loads(response.read()))
        ret_val.append(spec)
 
    return jsonify(r=ret_val)



@app.route('/mynamepost', methods=['POST'])
@app.route('/mynamepost/', methods=['POST'])
def myname_post():
    name = request.form.get('name', '')
    if name == '':
        name = 'William Conrad'
    return redirect('/%s/' % name)

    



