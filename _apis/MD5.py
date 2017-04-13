import hashlib

def md5(str):
	m = hashlib.md5()
	m.update(str)
	return m.hexdigest()

print md5(md5('admin') + 'yibao')