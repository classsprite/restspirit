# -*- coding=utf-8

from flask import Flask         #导入Flask类   
app = Flask(__name__)		#创建一个Flask类的实例

@app.route('/hello')
def hello():
    return 'Hello Xin!'

@app.route('/user/<username>')	#给url添加变量部分
def hello_user(username):		#将变量作为函数的参数
	return 'Hello %s' % username

@app.route('/post/<int:post_id>')#可以给变量限定数据类型
def show_post(post_id):				#将变量作为函数的参数
	return 'post_id %d' % post_id	

@app.route('/')			#设置路由，相当于设置函数入口
def hello_world():
    return 'Index Page'

@app.route('/projects/')		#这种情况下缺了末尾的/会自动补全
def projects():
	return 'the project page'

@app.route('/about')			#这种情况下缺了末尾的/会404
def about():
	return 'the about page'

if __name__ == '__main__':	#只有该文件被Python解释器直接执行的时候才运行
    app.run(debug=True)
