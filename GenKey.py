import os
try:
	from werkzeug.serving import make_ssl_devcert
except:
	print("No ssl module found... installing!")
	os.system("pip install pyopenssl")
	try:
		from werkzeug.serving import make_ssl_devcert
	except:
		print("Install failed... Try running terminal/cmd as admin/root and do pip install pyopenssl\nPress enter to continue")
make_ssl_devcert('Keys/ssl', host='localhost')