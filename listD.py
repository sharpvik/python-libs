#
# ================================         BBBBBB      YY    YYY           MMMM    MMMM    RRRRRR              VV      VVV    RRRRRR
# =             THE              =         BBB   BB     YY  YYY            MMMMM  MMMMM    RRR   RR             VV    VVV     RRR   RR
# ===> List functions library <===         BBBBBB        YYYYY             MMM  MM  MMM    RRRRRR                VV  VVV      RRRRRR
# =         (25.04.2018)         =         BBB   BBB      YYY              MMM      MMM    RRR  R                 VVVVV       RRR  R
# ================================         BBBBBBBB       YYY              MMM      MMM    RRR   RR                VVV        RRR   RR
#
# My github --> https://www.github.com/sharpvik <--
#



# imports
from random import randint
from functools import reduce



# functions

## --> unsorted function
def unsorted(length, low, high, format="list"): # length(int) -- number of elements you want to get; 
                                                # low(int) and high(int) -- limits for the generation of numeric elements; 
                                                # format(str) -- format of output (be default set to "list");
                                                # --> function returns unsorted list of numbers;
    lst = [ randint(low, high) for i in range(0, length) ]
    if format == "list":
        return lst
    else:
        for each in lst: 
            print(each, end=" ")
        print()
## unsorted function <--
