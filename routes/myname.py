
from app import app
from data.names import names
from flask import json, jsonify, redirect, render_template, request
from scripts.levenshtein import levenshtein3
import urllib2



@app.route('/<myname>')
@app.route('/<myname>/')
def myname(myname):
    for rd in names:
        rd['l2'] = levenshtein3(myname.lower(),rd['species'].lower())

    names.sort(key=lambda x:x['l2'], reverse=False)
    
    return render_template('myname.html', 
                            myname=myname, 
                            names=[x['species'] for x in names[0:20]])



@app.route('/mynamepost', methods=['POST'])
@app.route('/mynamepost/', methods=['POST'])
def myname_post():
    name = request.form.get('name', '')
    if name == '':
        name = 'William Conrad'
    return redirect('/%s/' % name)

    



