#
# ===============================         BBBBBB      YY    YYY           MMMM    MMMM    RRRRRR              VV      VVV    RRRRRR
# =             THE             =         BBB   BB     YY  YYY            MMMMM  MMMMM    RRR   RR             VV    VVV     RRR   RR
# ===> Combinatorics library <===         BBBBBB        YYYYY             MMM  MM  MMM    RRRRRR                VV  VVV      RRRRRR
# =        (26.04.2018)         =         BBB   BBB      YYY              MMM      MMM    RRR  R                 VVVVV       RRR  R
# ===============================         BBBBBBBB       YYY              MMM      MMM    RRR   RR                VVV        RRR   RR
#
# My gitgub --> https://www.github.com/sharpvik <--
#



# functions
def factorial(n):   # n(int) -- any positive number; --> function returns n!
    if n > 1:
        return factorial(n - 1) * n
    else:
        return 1



def nPr(n, r):      # n(int) -- number of items; r(int) -- number of positions; --> function returns the number of permutations of n elements for r positions 
    return int(factorial(n) / factorial(n - r))



def nCr(n, r):      # n(int) -- number of items; r(int) -- number of positions; --> function returns the number of combinations of n elements for r positions
    return int(factorial(n) / (factorial(n - r) * factorial(r)))
