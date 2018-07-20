import sqlite3
import json
import datetime
messages = []
def new_message(_text:str,_author:int):
	_mr = open("messages.json","r")
	_mw = open("messages.json","a")
	messages = json.loads(_mr.read())
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
	with open("users.json","r") as _users:
		_user_count = len(json.loads(_users.read()).keys())
		_users_loaded = json.loads(_users.read())
		_user = {
			"name": _name,
			"perms": _perms
		}
def get_messages():
	pass
