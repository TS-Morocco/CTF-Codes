#!/usr/bin/env python 3
import bcrypt
import base64

salt   = b'$2XXXXXXXXXXXXXXXXXXXX'
hashPass = b'$2XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

with open("rockyou.txt","r") as f:
	for word in f.readlines():
		passw = word.strip().encode('ascii', 'ignore')
		b64str = base64.b64encode(passw)
		hashAndSalt = bcrypt.hashpw(b64str, salt)
		#print(hashAndSalt)
		#print(passw)

		if hashPass == hashAndSalt:
			print("[+] Password Found!!!: %s" % passw)
			break
