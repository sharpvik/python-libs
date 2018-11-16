#
# ====================================         BBBBBB      YY    YYY           MMMM    MMMM    RRRRRR              VV      VVV    RRRRRR
# =               THE                =         BBB   BB     YY  YYY            MMMMM  MMMMM    RRR   RR             VV    VVV     RRR   RR
# ===> Divisors functions library <===         BBBBBB        YYYYY             MMM  MM  MMM    RRRRRR                VV  VVV      RRRRRR
# =           (26.04.2018)           =         BBB   BBB      YYY              MMM      MMM    RRR  R                 VVVVV       RRR  R
# ====================================         BBBBBBBB       YYY              MMM      MMM    RRR   RR                VVV        RRR   RR
#
# My github --> https://www.github.com/sharpvik <--
#



# imports
import math



# functions

def find(n, include=False, output_format="*"):      # n(int) -- any positive number; 
                                                    # include(bool, default=False) -- give True to include n as its own divisor;
                                                    # output_format(str, default="*") -- give "#" --> function returns number of divisors;
                                                    #                                 -- give "$" --> function return sum of the divisors;
                                                    #                                 -- don't give anything --> function returns sorted list of divisors;
    divisors = [1]                              
    for i in range( 2, int( math.sqrt(n) + 1 ) ):
        if i not in divisors and n % i == 0:
            divisors.append(i)
            if n // i not in divisors:
                divisors.append(n // i)
    divisors.sort()
    
    if output_format == "#":                    
        return len(divisors)
    elif output_format == "$":
        return sum(divisors)
    else:
        return divisors
