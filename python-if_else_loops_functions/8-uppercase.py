#!/usr/bin/python3
def uppercase(str):
    for c in str:
        uppercase_c = c
        if ord("a") <= ord(c) <= ord("z"):
            uppercase_c = chr(ord(c) - 32)
        print("{}".format(uppercase_c), end='')
    print()
