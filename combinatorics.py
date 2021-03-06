#
# ===============================         BBBBBB      YY    YYY           MMMM    MMMM    RRRRRR              VV      VVV    RRRRRR
# =             THE             =         BBB   BB     YY  YYY            MMMMM  MMMMM    RRR   RR             VV    VVV     RRR   RR
# ===> Combinatorics library <===         BBBBBB        YYYYY             MMM  MM  MMM    RRRRRR                VV  VVV      RRRRRR
# =        (26.04.2018)         =         BBB   BBB      YYY              MMM      MMM    RRR  R                 VVVVV       RRR  R
# ===============================         BBBBBBBB       YYY              MMM      MMM    RRR   RR                VVV        RRR   RR
#
# My github --> https://www.github.com/sharpvik <--
#



# functions

## --> factorial function
def factorial(n):   # n(int) -- any positive number; --> function returns n!;
    if not isinstance(n, int):
        raise ValueError("factorial() arg must be of type int")
    elif n < 0:
        raise ValueError("factorial() arg must be a positive number")
    elif n < 2:
        return 1
    else:
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f
## factorial function <--



## --> nPr function
def nPr(n, r):      # n(int) -- number of items; r(int) -- number of positions; --> function returns number of permutations of n elements for r positions;
    return int( factorial(n) / factorial(n - r) )
## nPr function <--



## --> nCr function
def nCr(n, r):      # n(int) -- number of items; r(int) -- number of positions; --> function returns number of combinations of n elements for r positions;
    return int( factorial(n) / ( factorial(n - r) * factorial(r) ) )
## nCr function <--



## --> anagrams function
def anagram(string):        # string(str) -- any string; --> function returns list of every possible arrangement of string;
    if len(string) == 0:
        return [string]
    else:
        anagrams = list()
        for word in anagram(string[1:]):
            for position in range( 0, len(word) + 1 ):
                anagrams.append(word[:position] + string[0] + word[position:])
        return anagrams
## anagrams function <--
