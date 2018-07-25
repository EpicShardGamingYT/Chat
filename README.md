# Chat
A open source chat app 






# SETUP


## Basic

### Setting up
	make shure you have python 3.6 (can be any 3 stable)
	make shure you have git and it added to path (see installer)
	run setup.py
	errors? pip install <modulename>
### Connect
	go on https://localhost:5000



## Advanced

### Custom GUI
	Simply drag and drop the page in the lib/GUI folder and it will be https://<URL>/<websitename>.
	the index file will just be / in the first dir

### Inerating with the API

	You can ineract with the api with requests EXAMPLE https://ghostbin.com/paste/whk4j
	List of api urls: 
		/lib/messages - Gets all messages in json form
		/lib/user/info/<ID> - gets info about a member
		/lib/user/create/<USERNAME>/<PASSWORD> - creates a user.
		/lib/user/send/<MESSAGE>/<TOKEN> - sends a message. Use a access token for this
		/lib/user/getSecret/<USERNAME>/<PASSWORD> - gets the users access token.