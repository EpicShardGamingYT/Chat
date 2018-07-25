from flask import *
import os
import time
from datetime import datetime
import requests
import json
import base64
import random
import lib
from OpenSSL import SSL
context = ('Keys/ssl.crt', 'Keys/ssl.key')
try:
	f = open("Keys/ssl.crt")
	f.close()
except:
	context = None
with open("settings.json") as f:
	settings = json.loads(f.read())
	f.close()


app = Flask(__name__)
app.config.from_object('config')



@app.route('/lib/user/getSecret/<string:username>/<string:pwd>')
def getSecret(username,pwd):
	return lib.database.security.get_token(username,pwd)

@app.route('/lib/user/send/<string:message>/<path:token>')
def send_message(message,token):
	author = lib.database.security.getID(token)
	lib.database.new_message(message,author)
	return ""
@app.route('/lib/user/create/<string:username>/<string:password>')
def create_user(username,password):
	lib.database.new_user(username,password,0)
	return ""
@app.route('/lib/user/info/<int:user>')
def user_info(user):
	return str(lib.database.lookup_user(user))

@app.route('/lib/messages')
def get_messages():
	return str(lib.database.get_messages())

@app.route('/')
def index():
	f = open("lib/gui/index.html")
	res = f.read()
	f.close()
	return res

















@app.route('/<path:page>')
def loadHtml(page):
	try:
		f = open("lib/gui/"+page+".html")
		res = f.read()
		f.close()
		return res
	except:
		f = open("lib/gui/404.html")
		res = f.read()
		f.close()
		return res






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=settings["port"],ssl_context=context)	