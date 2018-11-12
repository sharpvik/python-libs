#
# ================================         BBBBBB      YY    YYY           MMMM    MMMM    RRRRRR              VV      VVV    RRRRRR
# =             THE              =         BBB   BB     YY  YYY            MMMMM  MMMMM    RRR   RR             VV    VVV     RRR   RR
# ===> Math functions library <===         BBBBBB        YYYYY             MMM  MM  MMM    RRRRRR                VV  VVV      RRRRRR
# =         (08.05.2018)         =         BBB   BBB      YYY              MMM      MMM    RRR  R                 VVVVV       RRR  R
# ================================         BBBBBBBB       YYY              MMM      MMM    RRR   RR                VVV        RRR   RR
#
# My github --> https://www.github.com/sharpvik <--
#



# variables

pi = 3.1415926535897932384626433832795028841971693993751



# functions

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
    return x - (x // y * y) == 0
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
## additorial function <--



## --> power function ( logarithmic complexity )
def power(n, x):
    if x == 0: return 1
    if x == 1: return n 
    count = 1
    current = n
    while count * 2 < x:
        current *= current
        count *= 2
    for i in range(x - count): current *= n
    return current
## power function <--



## --> divisors function
def divisors(n):
	out = set()
	for i in range(1, n // 2 + 1):
		if i not in out and n % i == 0:
			out.add(i)
			out.add(n // i)
	out.remove(n)
	return out
## divisors function <--
