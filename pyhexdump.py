#!/usr/bin/env python3
__author__ = 'Karan'

import sys
import binascii
import textwrap

if len(sys.argv) > 1:
    f = open(sys.argv[1], "rb") #open the file to read as binary
    linenum = 1 #will count the linenumbers
    while True:
        line = f.read(16) #read 16 bytes
        if line == b"":
            break
        print(str(hex(linenum)[2:]).zfill(7), end=" ") #print line number in hex and pad it with 0s
        hexarray = binascii.hexlify(line).decode("utf-8") #convert it to hex from bytes
        array = " ".join(textwrap.wrap(hexarray, 2)) #group the string into group of 2s
        print(array)
        linenum += 1
    f.close()
else:
    print("Usage:pyhexdump.py <filename>")
