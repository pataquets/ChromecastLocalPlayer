#-*-coding:utf-8;-*-

from __future__ import print_function

import bottle, pychromecast
from bottle import request as req

import json, mimetypes #os, random

HOST = "0.0.0.0" # "localhost" # 
PORT = 8080 # random.randint(3001, 9999) # 

"""
Chromecast controller with Bottle Server UI
Requirements: bottle, pychromecast
"""

if __name__ == "__main__":
    try:              input = raw_input
    except NameError: pass

    print()
    print("Chromecast control app & local server by pychromecast & bottle.")

    from BottlePartialContent import app as local_server_app
    from ChromeCastControl import app as ccast_control_app

    server_url = "http://%s:%s" % (HOST,PORT)
    print()
    print("Server will run at %s" % server_url)

    print()
    ccast_control_app.merge(local_server_app)
    bottle.run(ccast_control_app, host=HOST, port=PORT)
