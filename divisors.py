#
# ====================================         BBBBBB      YY    YYY           MMMM    MMMM    RRRRRR              VV      VVV    RRRRRR
# =               THE                =         BBB   BB     YY  YYY            MMMMM  MMMMM    RRR   RR             VV    VVV     RRR   RR
# ===> Divisors functions library <===         BBBBBB        YYYYY             MMM  MM  MMM    RRRRRR                VV  VVV      RRRRRR
# =           (26.04.2018)           =         BBB   BBB      YYY              MMM      MMM    RRR  R                 VVVVV       RRR  R
# ====================================         BBBBBBBB       YYY              MMM      MMM    RRR   RR                VVV        RRR   RR
#
# My gitgub --> https://www.github.com/sharpvik <--
#



# imports
import math



# functions
def find(n, output_format="*"):                     # n(int) -- any positive number; 
                                                # output_format(str, default="*") -- give "#" --> function returns the number of divisors
                                                #                                 -- give "$" --> function return the sum of the divisors
                                                #                                 -- don't give anything --> function returns a sorted list of divisors

    divisors = [1]                              # change to ++> divisors = [1, n] <++ if you want to put number itself as its own divisor into the list
    for i in range(2, int(math.sqrt(n) + 1)):
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
