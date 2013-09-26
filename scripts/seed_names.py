'''
from scripts.seed_names import seed_names
seed_names()
'''


from db import db
from flask import json
import urllib2

def seed_names():
    collection = db['species']

    url = "http://www.antweb.org/api/?rank=species"
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    
    response_data = json.loads(response.read())

    data = {
            '_id':0,
            'data':response_data
            }
    collection.save(data)
