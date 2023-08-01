#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        firstChar = None
    else:
        firstChar = sentence[0]
    length = len(sentence)
    return length, firstChar
