#
# ==================================         BBBBBB      YY    YYY           MMMM    MMMM    RRRRRR              VV      VVV    RRRRRR
# =              THE               =         BBB   BB     YY  YYY            MMMMM  MMMMM    RRR   RR             VV    VVV     RRR   RR
# ===> String functions library <===         BBBBBB        YYYYY             MMM  MM  MMM    RRRRRR                VV  VVV      RRRRRR
# =          (26.04.2018)          =         BBB   BBB      YYY              MMM      MMM    RRR  R                 VVVVV       RRR  R
# ==================================         BBBBBBBB       YYY              MMM      MMM    RRR   RR                VVV        RRR   RR
#
# My github --> https://www.github.com/sharpvik <--
#



# functions

# --> reverse funcion
def reverse(string):            # string(str) -- any string; --> function returns reversed string;
    output = str()
    for i in range( len(string) - 1, -1, -1 ):
        output += string[i]
    return output
# reverse funciton <--



# --> remove_repeats function
def remove_repeats(string):     # string(str) -- any string; 
                                # --> function returns given string without repititions;
    return ''.join( set(string) )
# remove_repeats function <--
