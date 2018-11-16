#
# =================================         BBBBBB      YY    YYY           MMMM    MMMM    RRRRRR              VV      VVV    RRRRRR
# =             THE               =         BBB   BB     YY  YYY            MMMMM  MMMMM    RRR   RR             VV    VVV     RRR   RR
# ===>       Queue class       <===         BBBBBB        YYYYY             MMM  MM  MMM    RRRRRR                VV  VVV      RRRRRR
# =          (10.05.2018)         =         BBB   BBB      YYY              MMM      MMM    RRR  R                 VVVVV       RRR  R
# =================================         BBBBBBBB       YYY              MMM      MMM    RRR   RR                VVV        RRR   RR
#
# My github --> https://www.github.com/sharpvik <--
#



class Queue:                                # standard queue datatype;
    def __init__(self, element=None):
        if isinstance(element, None):
            self.storage = list()
        elif isinstance(element, list):
            self.storage = element
        else:
            self.storage = [element]

    def push(self, element):                # element(int / str) -- element you want to insert into the Queue;
                                            # --> function returns name of the inserted elment;
        self.storage.append(element)
        return element

    def pop(self):                          # --> function pops the first element you put into the Queue and returns its name;
        temp = self.storage[0]
        self.storage.pop(0)
        return temp

    def peek(self):                         # --> function returns the next value to be popped off of the Queue;
        try: return self.storage[0]
        except IndexError: pass
    
    def length(self):                       # --> function returns number of elements in the Queue;
        return len(self.storage)

    def is_empty(self):                     # --> function returns True if Queue is empty, otherwise, returns False;
        return self.length() == 0

    def inside(self, element):              # element(int / str) -- name of element you want to check for;
                                            # --> function returs True if element is in the Queue, otherwise, returns False;
        return element in self.storage
