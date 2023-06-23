#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (j > i) != 89:
            print("{:02d}, ".format(i+j), end='')
        else:
            print("{:02d}".format(i+j))
