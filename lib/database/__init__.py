import sqlite3
import json
import datetime
messages = []
def new_message(_text:str,_author:int):
	with open("messages.json","w") as _m:
		messages = json.loads(_m.read())
		_msg = {
			"time":datetime.datetime.now().time(),
			"content":_text,
			"author":_author
		}
		messages.append(_msg)
		_m.write(json.dump(messages))
		_m.close()
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
