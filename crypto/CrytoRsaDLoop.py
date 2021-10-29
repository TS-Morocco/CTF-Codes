#!/usr/bin/env python3
# Importing string library | Importation de la librarie "string"
import string
def main():
    # Strarting with an empty flag | De`marrage avec un flag vide
    flag = ''
    # Defining e n
    e = 65537
    n = 28...
    # Defining Encrypted Message | Definition du message crypte`
    encrypted_chars = [2876876...]
    # conditionnel double loop to print the flag
    for encrypted_char in encrypted_chars:
        for char in string.printable:
            if encrypted_char == pow(ord(char), e, n):
                flag += char
    print(flag)

if __name__ == '__main__':
    main()    
