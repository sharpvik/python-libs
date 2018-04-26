from random import randint

def create(length, sm, hi):
    array = []
    for a in range(0, length):
        array.append(randint(sm, hi))
    return array