#!/usr/bin/python3
for num in range(1, 100):
    if num % 3 != 0 and num % 5 != 0:
        print("{} ".format(num), end='')
    elif num % 3 == 0 and num % 5 != 0:
        print("Fizz ", end='')
    elif num % 3 != 0 and num % 5 == 0:
        print("Buzz ", end='')
    else:
        print("FizzBuzz ", end='')
