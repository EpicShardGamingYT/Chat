import sqlite3
import json
import datetime
import time
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
		_u = json.loads(users.read())
		try:
			_res = _u[_id]
			return _res
		except:
			return None
def new_user(_name:str,_perms:int):
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
def get_messages():
	pass
