import json
fileR = open("security.json","r")
sec = fileR.read()
fileR.close()

def setup_user(_uname,_pwd,_token):
	uob = json.loads(sec)
	user = {
		"uname": _uname,
		"pwd": _pwd,
		"token": _token
	}
	uob.append(user)
	fileW = open("security.json","w")
	fileW.write(json.dumps(uob))
def getID(_token):
	uob = json.loads(sec)
	for i in uob:
		if i["token"] == _token:
			with open("users.json") as f:
				l = json.loads(f.read())
				for b in l.keys():
					check = l[b]
					if check.name == b:
						return b
def get_token(_uname,_pwd):
	uob = json.loads(sec)
	_us = open("users.json")
	_us_obj = json.loads(_us.read())
	for i in _us_obj.keys():
		pass

		