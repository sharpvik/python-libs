#
# Functions for primes
#

from math import sqrt



def check(num):
    a = 2
    if num == a: return True # if num = 2 --> True
    elif num < a: return False # if num < 2 --> False
    else: # if num is different --> do
        while a <= int(sqrt(num)) + 1: # check if num is divisible by any number >= 2 and <= its square root 
                if num % a == 0: 
                    return False # and if yes --> False
                    break # kill the loop
                else:
                    a += 1 
        else:
            return True # this one is chosen --> True



def find(hi):
    working = []
    out = []

    for a in range(0, hi + 1): # make an array (working) with hi number of elements all True
        working.append(True)
    working[0] = working[1] = False # 0 and 1 are not primes --> False

    for c in range(2, hi + 1): 
        if working[c] and c ** 2 <= hi: # if current position of working array is True
            for d in range(c ** 2, hi + 1, c):
                working[d] = False

    for e in range(0, hi + 1): # go through the working 
        if working[e]: # find all the True positions
            out.append(e) # and put their indexs into the (out) array

    return out



def find_distincts(num):
    PRIMES = find(int(sqrt(num) + 1)) # now we've got all the primes that could possibly be divisors of num
    distincts = []
    num_to_test = num
    i = 0
    while not check(num_to_test): # while num_to_test is not prime itself
        if num_to_test % PRIMES[i] == 0: # we go through PRIMES and try find prime factors
            prime_factor = PRIMES[i] # and when we find one
            if prime_factor not in distincts: distincts.append(prime_factor) # and this one is not in the distincts list --> we append it there
            num_to_test /= prime_factor # and set num_to_test to be equal to previous value divided by this prime factor (regardles of its presense in the distincts list)
        else:
            i += 1 # if the current prime in PRIMES in not a divisor of the num_to_test we go to the next one
    else: 
        if num_to_test not in distincts: distincts.append(num_to_test) # when num_to_test becomes prime itself we put it into the distincts list if it is not already there
    return distincts


def find_number_of_distincts(num):
    return len(find_distincts(num))



def find_prime_factors(num):
    PRIMES = find(int(sqrt(num) + 1)) # now we've got all the primes that could possibly be divisors of num
    prime_factors = []
    num_to_test = num
    i = 0
    while not check(num_to_test): # while num_to_test is not prime itself
        if num_to_test % PRIMES[i] == 0: # we go through PRIMES and try find prime factors
            prime_factor = PRIMES[i] # and when we find one
            prime_factors.append(prime_factor) # we append it into the prime_factor list
            num_to_test /= prime_factor # and set num_to_test to be equal to previous value divided by this prime factor (regardles of its presense in the distincts list)
        else:
            i += 1 # if the current prime in PRIMES in not a divisor of the num_to_test we go to the next one
    else: 
        prime_factors.append(num_to_test) # when num_to_test becomes prime itself we put it into the
    return prime_factors
