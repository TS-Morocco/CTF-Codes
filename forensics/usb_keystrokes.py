import os,sys

newmap = {
    4: "a",
    5: "b",
    6: "c",
    7: "d",
    8: "e",
    9: "f",
    10: "g",
    11: "h",
    12: "i",
    13: "j",
    14: "k",
    15: "l",
    16: "m",
    17: "n",
    18: "o",
    19: "p",
    20: "q",
    21: 'r',
    22: 's',
    23: 't',
    24: 'u',
    25: 'v',
    26: 'w',
    27: 'x',
    28: 'y',
    29: 'z',
    30: '1',
    31: '2',
    32: '3',
    33: '4',
    34: '5',
    35: '6',
    36: '7',
    37: '8',
    38: '9',
    39: '0',
    40: '\r\n',
    41: 'ESC',
    42: "del",
    43: 'tab',
    44: 'space',
    45: '_',
    47: '[',
    48: ']',
    55: '*',
    56: '/',
    57: 'CapsLock',
    79: '>',
    0: "",
    80: '<'
}


#if len(sys.argv) != 2:


try:
    if ".txt" in sys.argv[1] :
        mykeys = open(sys.argv[1])
    else:
        os.system(f"tshark -r ./{sys.argv[1]} -T fields -e usb.capdata| tr -d : > temp.txt")
        mykeys = open("temp.txt")
        os.system("rm temp.txt")
        
    message = ""
    
    for line in mykeys:
        bytesArray = bytearray.fromhex(line.strip())
        
        for byte in bytesArray:
            if byte != 0:
                print (f"Debug Byte = {str(byte)}")
                keyVal = int(byte)
                if keyVal in newmap:
                    print (newmap[keyVal])
                    if bytesArray[0] == 2:
                        message += newmap[keyVal].upper()
                    else :
                        message += newmap[keyVal]
    
                else:
                    pass
    
    print (message)
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




            |-----------------------------------------------|
    Syntax > python3 {sys.argv[0]} packets.pcap
             -------------------------------
             python3 {sys.argv[0]} capdata.txt
            |-----------------------------------------------|

   

    """)

