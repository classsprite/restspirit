import hashlib, base64

def md5(str):
	m = hashlib.md5()
	m.update(str)
	return m.hexdigest()

print md5(md5('admin') + 'abcd')#940eace6ed64673b5de2ea7976a57685
print base64.b64encode('admin') 		  #YWRtaW4=


