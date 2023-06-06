#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastDigit = abs(number) % 10
    lastDigit = lastDigit - (lastDigit * 2)
elif number >= 0: 
    lastDigit = abs(number) % 10
if lastDigit == 0:
    print('Last digit of', number, 'is', lastDigit, "and "
     "is 0")
elif lastDigit > 5:
    print('Last digit of', number, 'is', lastDigit, "and "
        "is greater than 5")
else:
    print('Last digit of', number, 'is', lastDigit, "and "
        "is less than 6 and not 0")
