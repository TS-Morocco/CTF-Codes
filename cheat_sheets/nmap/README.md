# nmap Cheat sheet

<details>
<summary> Target Specification </summary>

|Description      |Example    |
|-----------------|---------------|
|Scan a single IP	|nmap 192.168.1.1|
|Scan a host	|nmap www.testhostname.com|
|Scan a range of IPs	|nmap 192.168.1.1-20|
|Scan a subnet	|nmap 192.168.1.0/24|
|Scan targets from a text file	|nmap -iL list-of-ips.txt|

</details>

<details>
<summary> Port Selection </summary>

|Description      |Example    |
|-----------------|---------------|
|Scan a single Port	|nmap -p 22 192.168.1.1|
|Scan a range of ports	|nmap -p 1-100 192.168.1.1|
|Scan 100 most common ports (Fast)	|nmap -F 192.168.1.1|
|Scan all 65535 ports	|nmap -p- 192.168.1.1|

</details>



<details>
<summary> Port Scan types</summary>

|Description      |Example    |
|-----------------|---------------|
|Scan using TCP connect	|nmap -sT 192.168.1.1|
|Scan using TCP SYN scan (default)	|nmap -sS 192.168.1.1|
|Scan UDP ports	|nmap -sU -p 123,161,162 192.168.1.1|
|Scan selected ports - ignore discovery	|nmap -Pn -F 192.168.1.1|
</details>

<details>
<summary> Service and OS Detection </summary>

|Description      |Example    |
|-----------------|---------------|
|Detect OS and Services	|nmap -A 192.168.1.1|
|Standard service detection	|nmap -sV 192.168.1.1|
|More aggressive Service Detection	|nmap -sV --version-intensity 5 192.168.1.1|
|Lighter banner grabbing detection	|nmap -sV --version-intensity 0 192.168.1.1|


</details>

<details>
<summary> Output Formats </summary>

|Description      |Example    |
|-----------------|---------------|
|Save default output to file	|nmap -oN outputfile.txt 192.168.1.1|
|Save results as XML	|nmap -oX outputfile.xml 192.168.1.1|
|Save results in a format for grep	|nmap -oG outputfile.txt 192.168.1.1|
|Save in all formats	|nmap -oA outputfile 192.168.1.1|

</details>

<details>
<summary> NSE Scripts </summary>

|Description      |Example    |
|-----------------|---------------|
|Scan using default safe scripts	|nmap -sV -sC 192.168.1.1|
|Get help for a script	|nmap --script-help=ssl-heartbleed|
|Scan using a specific NSE script	|nmap -sV -p 443 –script=ssl-heartbleed.nse 192.168.1.1|
|Scan with a set of scripts	|nmap -sV --script=smb* 192.168.1.1|

</details>