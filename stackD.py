#
# =================================         BBBBBB      YY    YYY           MMMM    MMMM    RRRRRR              VV      VVV    RRRRRR
# =             THE               =         BBB   BB     YY  YYY            MMMMM  MMMMM    RRR   RR             VV    VVV     RRR   RR
# ===>       Stack class       <===         BBBBBB        YYYYY             MMM  MM  MMM    RRRRRR                VV  VVV      RRRRRR
# =          (10.05.2018)         =         BBB   BBB      YYY              MMM      MMM    RRR  R                 VVVVV       RRR  R
# =================================         BBBBBBBB       YYY              MMM      MMM    RRR   RR                VVV        RRR   RR
#
# My gitgub --> https://www.github.com/sharpvik <--
#



class Stack:                                # standard stack datatype;
    def __init__(self, element=None):
        if isinstance(element, list):
            self.storage = element
        else:
            self.storage = [element]
        
    def push(self, element):                # element(int / str) -- element you want to add into the Stack;
                                            # --> function returns name of the added elment;
        self.storage.append(element)
        return element

    def pop(self):                          # --> function pops the last element you put into the Stack and returns its name;
        temp = self.storage[-1]
        self.storage.pop(-1)
        return temp

    def last(self):                          # --> function returns the last value pushed to the Stack;
        return self.storage[-1]

    def length(self):                       # --> function returns number of elements in the Stack;
        return len(self.storage)

    def inside(self, element):              # element(int / str) -- name of element you want to check for;
                                            # --> function returs True if element is in the Stack, otherwise, returns False;
        return element in self.storage
