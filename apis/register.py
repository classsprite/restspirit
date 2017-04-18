# coding=utf-8
from flask import Flask, request
from random import Random
import psycopg2, hashlib

app = Flask(__name__)

@app.route('/register/', methods=['POST'])
def register():
	if request.method == 'POST':
		role = request.headers.get('role')							#身份				
		email = request.headers.get('email')						#邮箱
		username = request.headers.get('username')					#用户名
		password = request.headers.get('password')					#密码
		no = request.headers.get('no')								#学号/工号
		department = request.headers.get('department')				#院系
		grade_or_title = request.headers.get('grade_or_title')		#年级或职称

		salt = create_salt()										#盐值
		password = md5(md5(password) + salt)  						#加盐加密
		
		conn = psycopg2.connect(database="ktjl", user="postgres", password="admin", host="127.0.0.1", port="5432")
		cur = conn.cursor()
		
		#存储注册信息(需要检查是否已经存在)
		cur.execute('''INSERT INTO public.users (no, type, email, username, password) 
			VALUES (%s, %s, %s, %s, %s);''' , (no, role, email, username, password))
		conn.commit()

		#获取用户id
		cur.execute('''SELECT id FROM public.users WHERE no = '%s';''', (no,))
		conn.commit()		
		uid = cur.fetchall()[0][0]

		#存储盐值
		cur.execute('''INSERT INTO public.salt (uid, salt) VALUES (%s, %s)''', (uid, salt))
		conn.commit()

		#存储用户信息
		cur.execute('''INSERT INTO public.user_info (id, department) VALUES (%s, %s);''', (uid, department))
		conn.commit()

		#更新学生/教师表
		if role == 's':
			cur.execute('''INSERT INTO public.student (sid, grade) VALUES (%s, %s);''', (uid, grade_or_title))
			conn.commit()
		else:
			cur.execute('''INSERT INTO public.teacher (tid, title) VALUES (%s, %s);''', (uid, grade_or_title))
			conn.commit()	

		cur.close()
		conn.close()

	return 0

def md5(str):
	m = hashlib.md5()
	m.update(str)
	return m.hexdigest()

def create_salt(length = 4):  
	salt = ''  
	chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'  
	len_chars = len(chars) - 1  
	random = Random()  
	for i in xrange(length):  
		# 每次从chars中随机取一位  
		salt += chars[random.randint(0, len_chars)]  
	return salt  

if __name__ == '__main__':
	app.run(debug=True)