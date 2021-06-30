#!/usr/bin/env python3

import sys
from factordb.factordb import FactorDB
from Crypto.Util.number import inverse

def get_p_q(n):
    f = FactorDB(n)
    f.connect()
    return f.get_factor_list()

def get_d (e,p,q):
    t = get_t(p,q)
    return inverse(e,t)

def get_t(p,q):
    return (1-p)*(1-q)

def message(c,d,n):
    m = pow(c,d,n)

    # Cause some CTFs might need the undecoded RSA 

    result = f"""
result without Decoding : 

{m}


result with Decoding :


{bytes.fromhex(hex(m)[2:])}

    """
    return result


def Solver(data):
    c = data["c"] 
    e = data["e"] 
    n = data["n"] 

    if "d" not in data.keys():
        pq  = get_p_q(n)
        p = pq[0]
        q = pq[1]
        return message(c,get_d(e,p,q),n)
    else :
        d = data["d"]
        return message(c,d,n)


def get_data():
    # get the data from file ( n , d, c, e, p , q )
    with open(sys.argv[1]) as f :   
        lines = f.read().splitlines()
    
    
    # Turn the list to dict
    _dict = dict()
    for i in lines:
        _dict[i.split("=")[0]] = eval(i.split("=")[1])

    return _dict

if __name__ == "__main__":
    try:
        data = get_data()
        print (Solver(data))
    except:
        print (f"""

  _____     _  ____  _    _ _____ _____  _____ 
 |_   _|   | |/ __ \| |  | |_   _|  __ \|_   _|
   | |     | | |  | | |  | | | | | |__) | | |  
   | | _   | | |  | | |  | | | | |  _  /  | |  
  _| || |__| | |__| | |__| |_| |_| | \ \ _| |_ 
 |_____\____/ \____/ \____/|_____|_|  \_\_____|
                                               
                                               Project : https://github.com/TSRI-Casa/CTF-Codes/
                                               Github  : https://github.com/ijouiri

                                               


            |------------------------------------|
                Syntax : python3 {sys.argv[0]} file 
            |------------------------------------|

File example :

                e=3
                c=219878849218803628752496734037301843801487889344508611639028
                n=245841236512478852752909734912575581815967630033049838269083

""")
