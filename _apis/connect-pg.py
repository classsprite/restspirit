import psycopg2

conn = psycopg2.connect(database="ktjl", user="postgres", password="admin", host="127.0.0.1", port="5432")
cur = conn.cursor()
no = '1000000003'
role = 's'
email = 'test@test.com'
username = 'test3'
password = 'asghfg'

name = 'tesfghjt'

#mogrify
cur.execute("SELECT id FROM public.users WHERE username = '%s';" % (name, ))
rows = cur.fetchall()        # all rows in table
print(rows[0][0])
print(len(rows))
conn.commit()
cur.close()
conn.close()
