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
def pow(n, p):                  # n(int / float) -- any number; p(int) -- power of your number has to be >= 1
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
