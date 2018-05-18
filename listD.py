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
def unsorted(length, low, high):        # length(int) -- number of elements you want to get; low(int) and high(int) -- limits for the generation of numeric elements; 
                                        # --> function returns unsorted list of numbers;
    array = []
    for i in range(0, length):
        array.append( randint(low, high) )
    return array
## unsorted function <--



## --> present_in function
def present_in(array, element):         # array(list) -- list that we want to check for presence of element;
                                        # element(any datatype) -- element we want to check for presence in array;
                                        # --> function returns True if element is in array, otherwise, returns False;
    for each in array:
        if element == each:
            return True
    else:
        return False
## present_in funciton <--



## --> lsum function
def lsum(array):
    return reduce(lambda a, b: a + b, array)
## lsum function <--
