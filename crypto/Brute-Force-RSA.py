#!/usr/bin/env python3
import string
def main():
    flag = ''
    e = 65537
    n = 28...
    encrypted_chars = [2876876...]
    for encrypted_char in encrypted_chars:
        for char in string.printable:
            if encrypted_char == pow(ord(char), e, n):
                flag += char
    print(flag)
    
if __name__ == '__main__':
    main()
    
