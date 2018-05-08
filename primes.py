#
# ==================================         BBBBBB      YY    YYY           MMMM    MMMM    RRRRRR              VV      VVV    RRRRRR
# =              THE               =         BBB   BB     YY  YYY            MMMMM  MMMMM    RRR   RR             VV    VVV     RRR   RR
# ===> Primes functions library <===         BBBBBB        YYYYY             MMM  MM  MMM    RRRRRR                VV  VVV      RRRRRR
# =          (26.04.2018)          =         BBB   BBB      YYY              MMM      MMM    RRR  R                 VVVVV       RRR  R
# ==================================         BBBBBBBB       YYY              MMM      MMM    RRR   RR                VVV        RRR   RR
#
# My gitgub --> https://www.github.com/sharpvik <--
#



# imports
from math import sqrt



# functions

## --> check if prime
def check(n):                           # n(int) -- any positive number; --> function returns True or False;
    a = 2
    if n == a: return True              # if n = 2 --> True;
    elif n < a: return False            # if n < 2 --> False;
    else:                               # if n is different --> do;
        while a <= int( sqrt(n) ) + 1:  # check if n is divisible by any number >= 2 and <= its square root; 
                if n % a == 0: 
                    return False        # and if yes --> False;
                    break               # kill the loop;
                else:
                    a += 1 
        else:
            return True                 # this one is chosen --> True;
## check if prime <--



## --> find primes within a limit
def find(limit):                                        # limit(int) -- any positive number; --> function returns list of primes;
    working = []
    output = []

    for a in range(0, limit + 1):                       # make an array (working) with limit number of elements all True;
        working.append(True)
    working[0] = working[1] = False                     # 0 and 1 are not primes --> False;

    for b in range(2, limit + 1): 
        if working[b] and b ** 2 <= limit:              # if current position of working array is True;
            for c in range(b ** 2, limit + 1, b):
                working[c] = False

    for d in range(0, limit + 1):                       # go through the working; 
        if working[d]:                                  # find all the True positions;
            output.append(d)                            # and put their indexs into the (output) array;

    return output
## find primes within a limit <--



## --> find distinct prime divisors 
def find_distincts(n, output_format="*"):                                       # n(int) -- any positive number; 
                                                                                # output_format(str, default="*") -- give "#" --> function returns number of distinct prime divisors;
                                                                                #                                 -- don't give anything --> function returns list of distinct prime divisors;

    primes = find( int( sqrt(n) + 1 ) )                                         # now we've got all the primes that could possibly be divisors of n;
    distincts = []
    num_to_test = n
    i = 0
    while not check(num_to_test):                                               # while num_to_test is not prime itself;
        if num_to_test % primes[i] == 0:                                        # we go through primes and try find prime factors;
            prime_factor = primes[i]                                            # and when we find one;
            if prime_factor not in distincts: distincts.append(prime_factor)    # and this one is not in the distincts list --> we append it there;
            num_to_test /= prime_factor                                         # and set num_to_test to be equal to previous value divided by this prime factor (regardles of its presense in the distincts list);
        else:
            i += 1                                                              # if the current prime in primes in not a divisor of the num_to_test we go to the next one;
    else: 
        if num_to_test not in distincts: distincts.append( int(num_to_test) )   # when num_to_test becomes prime itself we put it into the distincts list if it is not already there;
    
    if output_format == "#":
        return len(distincts)
    else:
        return distincts
## find distinct prime divisors <--



## --> find prime factors
def find_prime_factors(n):                          # n(int) -- any positive number; --> function returns list of prime factors of n;

    primes = find( int( sqrt(n) + 1 ) )             # now we've got all the primes that could possibly be divisors of n;
    prime_factors = []
    num_to_test = n
    i = 0
    while not check(num_to_test):                   # while num_to_test is not prime itself;
        if num_to_test % primes[i] == 0:            # we go through primes and try find prime factors;
            prime_factor = primes[i]                # and when we find one;
            prime_factors.append(prime_factor)      # we append it into the prime_factor list;
            num_to_test /= prime_factor             # and set num_to_test to be equal to previous value divided by this prime factor (regardles of its presense in the distincts list);
        else:
            i += 1                                  # if the current prime in primes in not a divisor of the num_to_test we go to the next one;
    else: 
        prime_factors.append( int(num_to_test) )    # when num_to_test becomes prime itself we put it into the prime_factors;
    return prime_factors
## find prime factors <--
