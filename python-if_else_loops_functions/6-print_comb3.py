#!/usr/bin/python3
for i in range(10):
    for j in range(1, 10):
        if (j > i):
            print(i, end='')
            print(j, end='')
            if (j>i and i!= 8):
                print(", ", end='')
            else:
                print("")
