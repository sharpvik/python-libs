#
# ================================         BBBBBB      YY    YYY           MMMM    MMMM    RRRRRR              VV      VVV    RRRRRR
# =             THE              =         BBB   BB     YY  YYY            MMMMM  MMMMM    RRR   RR             VV    VVV     RRR   RR
# ===> List functions library <===         BBBBBB        YYYYY             MMM  MM  MMM    RRRRRR                VV  VVV      RRRRRR
# =         (25.04.2018)         =         BBB   BBB      YYY              MMM      MMM    RRR  R                 VVVVV       RRR  R
# ================================         BBBBBBBB       YYY              MMM      MMM    RRR   RR                VVV        RRR   RR
#
# My gitgub --> https://www.github.com/sharpvik <--
#



# imports
from random import randint
from functools import reduce



# functions

## --> unsorted function
def unsorted(length, low, high):        # length(int) -- number of elements you want to get; 
                                        # low(int) and high(int) -- limits for the generation of numeric elements; 
                                        # --> function returns unsorted list of numbers;
    return [ randint(low, high) for i in range(0, length) ]
## unsorted function <--



## --> lsum function
def lsum(array):                        # array(list of int / float) -- list of numbers that you want to sum;
    return reduce(lambda a, b: a + b, array)
## lsum function <--
