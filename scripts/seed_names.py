'''
from scripts.seed_names import seed_names
seed_names()
'''



from flask import json
import urllib2

def seed_names():

    print 'seed_names'
    url = "http://www.antweb.org/api/?rank=species"
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    
    response_data = json.loads(response.read())

    f = open('data/names.py', 'w')
    print f
    f.write('names=%s' % str(response_data))
    f.close()
