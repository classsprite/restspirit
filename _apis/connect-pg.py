import psycopg2
conn = psycopg2.connect(database="ktjl", user="postgres", password="admin", host="127.0.0.1", port="5432")
cur = conn.cursor()
no = '1000000003'
role = 's'
email = 'test@test.com'
username = 'test3'
password = 'asghfg'

#mogrify
cur.execute('''INSERT INTO public.users (no, type, email, username, password) 
	VALUES (%s, %s, %s, %s, %s);''' , (no, role, email, username, password) )
#rows = cur.fetchall()        # all rows in table
#print(rows)
conn.commit()
cur.close()
conn.close()
