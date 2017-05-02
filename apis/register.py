# coding=utf-8
from flask import Flask, request
from random import Random
import psycopg2, hashlib
import start.py

#app = Flask(__name__)

#retuan ans(String)
#-1		用户名已经被注册
#0		注册成功

@app.route('/register/', methods=['POST'])
def register():
	if request.method == 'POST':
		log = ""
		role = request.form.get('role')							#身份				
		email = request.form.get('email')						#邮箱
		username = request.form.get('username')					#用户名
		password = request.form.get('password')					#密码
		no = request.form.get('no')								#学号/工号
		department = request.form.get('department')				#院系
		grade_or_title = request.form.get('grade_or_title')		#年级或职称

		salt = create_salt()										#盐值
		password = md5(md5(password) + salt)  						#加盐加密
		
		conn = psycopg2.connect(database="ktjl", user="postgres", password="admin", host="127.0.0.1", port="5432")
		cur = conn.cursor()
		
		ans = ""
		#查询该用户名是否存在
		cur.execute("SELECT id FROM public.users WHERE username = '%s';" % (username,)) 
		conn.commit()
		rows = cur.fetchall()        # all rows in table
		if len(rows) == 0:											#没被注册
			#存储用户通用信息
			cur.execute('''INSERT INTO public.users (no, type, email, username, password) 
				VALUES (%s, %s, %s, %s, %s);''' , (no, role, email, username, password))
			conn.commit()

			#获取用户id
			cur.execute("SELECT id FROM public.users WHERE username = %s;", (username,))
			conn.commit()		
			uid = cur.fetchall()[0][0]

			#存储盐值
			cur.execute('''INSERT INTO public.salt (uid, salt) VALUES (%s, %s);''', (uid, salt))
			conn.commit()

			#存储用户信息
			cur.execute('''INSERT INTO public.user_info (uid, department) VALUES (%s, %s);''', (uid, department))
			conn.commit()

			#更新学生/教师表
			if role == 's':
				cur.execute('''INSERT INTO public.student (sid, grade) VALUES (%s, %s);''', (uid, grade_or_title))
				conn.commit()
			else:
				cur.execute('''INSERT INTO public.teacher (id, title) VALUES (%s, %s);''', (uid, grade_or_title))
				conn.commit()	

			ans = "0"
		else :
			ans = "-1"

		cur.close()
		conn.close()

	return ans

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

#if __name__ == '__main__':
#	app.run(debug=True)
