#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        a, b = (0, 0)
    elif len(tuple_a) == 1:
        a = tuple_a[0]
        b = 0
    else:
        a = tuple_a[0]
        b = tuple_a[1]
    if len(tuple_b) == 0:
        a2, b2 == (0, 0)
    elif len(tuple_b) == 1:
        a2 = tuple_b[0]
        b2 = 0
    else:
        a2 = tuple_b[0]
        b2 = tuple_b[1]
    tuple_ab = (a + a2, b + b2)
    return tuple_ab
