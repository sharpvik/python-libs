# python divisors.py

import math

def find(num, ret):
    divs = [1] # change to [1, num] if you want to put number itself as its own divisor into the list
    for a in range(2, int(math.sqrt(num) + 1)):
        if a not in divs and num % a == 0:
            divs.append(a)
            if num // a not in divs:
                divs.append(num // a)
    divs.sort()
    
    if ret == "num":
        return len(divs)
    elif ret == "sum":
        return sum(divs)
    else:
        return divs