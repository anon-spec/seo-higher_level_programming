#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord("a") <= ord(c) <= ord("z"):
            uppercase_c = chr(ord(c) - 32)
            print("{}".format(uppercase_c), end='')
        else: 
            print(c, end='')
    print()
