'''
A simple Python script to make the characters appear one after the other on the terminal, giving that cool movie hacky effect!
'''

#!/usr/bin/env python
from time import *
import os, sys

char_start = 0
char_end = 1

string = str(sys.argv[2]) # Read input from command line

if len(sys.argv) > 1: #checks for command line arguments
    delay = float( sys.argv[1] ) #uses argument as delay time

else:
    delay = 0.10

strlength = len(string)+1

print ""

while char_end <= strlength:
    printchar = string[char_start:char_end]
    sys.stdout.write(printchar)
    sys.stdout.flush()
    sleep(delay) # delay time between characters
    char_end += 1
    char_start += 1

print "\n"

exit

