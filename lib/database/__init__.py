import sqlite3
import json
import datetime
import time
from . import Security as security
import string
import random
import json
tokenLen = 30
messages = []
def new_message(_text:str,_author:int):
	_mr = open("messages.json","r")
	messages = json.loads(_mr.read())
	_mw = open("messages.json","w")
	_msg = {
		"time":str(datetime.datetime.now().time()),
		"content":_text,
		"author":_author
	}
	messages.append(_msg)
	_mw.write(json.dumps(messages))
	_mr.close()
	_mw.close()
def lookup_user(_id: int):
	with open("users.json","r") as _users:
		_u = json.loads(_users.read())
		try:
			_res = _u[str(_id)]
			return _res
		except:
			return ""
def new_user(_name:str,_pwd:str,_perms:int):
	_users = open("users.json")
	_us = json.loads(_users.read())
	_user_count = len(_us.keys())
	_users_loaded = _us
	_user = {
		"name": _name,
		"perms": _perms
	}
	_users_loaded[_user_count+1] = _user
	_users.close()
	_users = open("users.json","w")
	_users.write(json.dumps(_users_loaded))
	_users.close()
	_token = []
	for i in range(tokenLen+1):
		_token.append(random.choice(string.printable))
	_token.remove(" ")
	security.setup_user(_name,_pwd,"".join(_token))
def get_messages():
	_file = open("messages.json")
	res = json.loads(_file.read())
	_file.close()
	return res
