# coding=utf-8
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello():
    text = request.args.get('text')
    temp = request.args.get('temp')
    return 'hello %s  %s' % (text, temp)


if __name__ == '__main__':
	app.run(debug=True)