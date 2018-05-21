#
# ================================         BBBBBB      YY    YYY           MMMM    MMMM    RRRRRR              VV      VVV    RRRRRR
# =             THE              =         BBB   BB     YY  YYY            MMMMM  MMMMM    RRR   RR             VV    VVV     RRR   RR
# ===> Math functions library <===         BBBBBB        YYYYY             MMM  MM  MMM    RRRRRR                VV  VVV      RRRRRR
# =         (08.05.2018)         =         BBB   BBB      YYY              MMM      MMM    RRR  R                 VVVVV       RRR  R
# ================================         BBBBBBBB       YYY              MMM      MMM    RRR   RR                VVV        RRR   RR
#
# My gitgub --> https://www.github.com/sharpvik <--
#



# functions

## --> power function
def power(n, p):                  # n(int / float) -- any number; p(int) -- power of your number has to be >= 1
    if p == 0:
        return 1
    elif p == 1:
        return n
    elif p == 2:
        return n * n
    else:
        return pow(n, p // 2) * pow(n, p - p // 2)
## power function <--



## --> fibonacci function
def fib(index):                 # index(int) -- position of number in fibonacci sequence that you want to find;
                                # --> function returns fibonacci number with given index if index is positive;
                                # --> otherwise returns -1
    if index < 0:
        return -1
    if index <= 1:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)
## fibonacci function <--



## --> modulo function
def mod(x, y):                  # x(int) and y(int) -- any numbers
    return x - (x // y * y)
## modulo function



## --> intersection function
def intersect(x, y):            # s(list / set) and y(list / set) -- any two lists you want to get intersection of
                                # --> function returns a set that contains the intersection of the lists you gave it
    output = set()
    for each in x:
        if each in y:
            output.add(each)
    return output
## intersection function <--



## --> coprimes function
def coprimes(n, p, q):          # n(int) = p * q -- any number that is a product of two primes; p(int) and q(int) -- prime factors of n;
                                # --> function returns the list of coprimes of n;

    def remover(a, i):          # *** internal use ***
        c = 1
        while i * c <= n:
            try:
                a.remove(i * c)
            except ValueError:
                pass
            c += 1
        return a

    return remover( remover( list( range(1, n + 1) ), p ), q )
## coprimes function <--



## --> greatest common divisor function
def gcd(a, b):                  # a(int) and b(int) -- any numbers;
                                # --> function returns greatest common divisor of a and b;
    return a if b == 0 else gcd(b, a % b)
## greatest common divisor function <--



## --> floor function
def floor(f):
    return int(f) + 1 if f % int(f) >= 0.5 else int(f)
## floor function <--



## --> additorial fucntion
def additorial(n):              # n(int) -- any positive number;
                                # --> function returns sum of all numbers from one to n, including n itself;
                                # example:  additorial(4) = 4 + 3 + 2 + 1 = 10
                                # general formula: additorial(n) = n + n-1 + n-2 + ... + 1
    return sum( list( range(n + 1) ) )
## additorial function



## --> divisible function
def divisible(n, d):            # n(int / float) -- any number; d(int / float) -- any number;
                                # --> function returns True if n is divisible by d, otherwise returns False;
    return True if n % d == 0 else False
## divisible function <--