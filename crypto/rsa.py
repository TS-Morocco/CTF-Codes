#!/usr/bin/env python3

import sys
from factordb.factordb import FactorDB
from Crypto.Util.number import inverse
#

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
    return bytes.fromhex(hex(m)[2:])


def Solver(data):
    c = data["c"] 
    e = data["e"] 
    n = data["n"] 

    if "p" and "q" not in data.keys():
        pq  = get_p_q(n)
        p = pq[0]
        q = pq[1]

    return message(c,get_d(e,p,q),n)

    #elif option == "t":
    #    return (1-p) * (1-q)
    #        

    #elif option == "n":
    #    return q * p
    #        
    #elif option == "c":
    #    return pow(m,e,n)

    #elif option == "d":
    #    return inverse(e,t)


def get_data():
    # get the data from file ( n , d, c, ...)
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f :   
            lines = f.read().splitlines()
        
        
        # Turn the list to dict
        _dict = dict()
        for i in lines:
            _dict[i.split("=")[0]] = int(i.split("=")[1])

        return _dict
    else:

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

if __name__ == "__main__":

    data = get_data()
    #data = {
    #    "e":3,
    #    "c":219878849218803628752496734037301843801487889344508611639028,
    #    "n":245841236512478852752909734912575581815967630033049838269083
    #}

    print (data)
    print (Solver(data))
    
    
