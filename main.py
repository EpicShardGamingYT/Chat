from flask import *
import os
import time
from datetime import datetime
import requests
import json
import base64
import random
import lib
app = Flask(__name__)
app.config.from_object('config')





@app.route('/lib/send/<string:message>/<int:author>')
def send_message(message,author):
	lib.database.new_message(message,author)
	return ""



























if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))