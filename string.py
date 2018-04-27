#
# ==================================         BBBBBB      YY    YYY           MMMM    MMMM    RRRRRR              VV      VVV    RRRRRR
# =              THE               =         BBB   BB     YY  YYY            MMMMM  MMMMM    RRR   RR             VV    VVV     RRR   RR
# ===> String functions library <===         BBBBBB        YYYYY             MMM  MM  MMM    RRRRRR                VV  VVV      RRRRRR
# =          (26.04.2018)          =         BBB   BBB      YYY              MMM      MMM    RRR  R                 VVVVV       RRR  R
# ==================================         BBBBBBBB       YYY              MMM      MMM    RRR   RR                VVV        RRR   RR
#
# My gitgub --> https://www.github.com/sharpvik <--
#



# functions
def reverse(string):        # string(str) -- any string; --> function returns a reversed string
    output = []
    for i in range(len(string) - 1, -1, -1):
        output.append(string[i])
    return ''.join(output)
