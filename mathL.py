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

# --> power function
def power(n, p):            # n(int / float) -- any number; p(int) -- power of your number has to be >= 1
    if p == 0:
        return 1
    elif p == 1:
        return n
    elif p == 2:
        return n * n
    else:
        return pow(n, p // 2) * pow(n, p - p // 2)
# power function <--



# --> fibonacci function
def fibonacci(index):       # index(int) -- position of number in fibonacci sequence that you want to find;
                            # --> function returns fibonacci number with given index if index is positive;
                            # --> otherwise returns -1
    if index < 0:
        return -1
    if index <= 1:
        return 1
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)
# fibonacci function <--
