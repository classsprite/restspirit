import hashlib, base64

def md5(str):
	m = hashlib.md5()
	m.update(str)
	return m.hexdigest()

print md5(md5('admin') + 'n75T')#1ee55bf4e048d2d7c960ed95aa031e78
print base64.b64encode('admin') 		  #YWRtaW4=


