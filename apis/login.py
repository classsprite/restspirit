# coding=utf-8
from flask import Flask, requset
app = Flask(__name__)

@app.route('/login/', methods=['GET'])
def login():
	if requset.method == 'GET':
		if()

if __name__ == '__main__':
	app.run(debug=True)