from app import app
from flask import json, jsonify, render_template




@app.route('/species/<species_name>')
@app.route('/species/<species_name>/')
def species_name_root(species_name):
    import urllib2
    url = "http://www.antweb.org/api/?rank=species&name=%s" % species_name
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    specimens = json.loads(response.read())
    if specimens == 'No records found.':
        return 'No records found.'

    #return jsonify(d=specimens)
    return render_template('specimen.html',
                            speciesName=species_name,
                            specimens=specimens)
