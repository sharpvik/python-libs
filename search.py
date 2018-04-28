#
# ==================================         BBBBBB      YY    YYY           MMMM    MMMM    RRRRRR              VV      VVV    RRRRRR
# =              THE               =         BBB   BB     YY  YYY            MMMMM  MMMMM    RRR   RR             VV    VVV     RRR   RR
# ===> Search functions library <===         BBBBBB        YYYYY             MMM  MM  MMM    RRRRRR                VV  VVV      RRRRRR
# =         (25.04.2018)           =         BBB   BBB      YYY              MMM      MMM    RRR  R                 VVVVV       RRR  R
# ==================================         BBBBBBBB       YYY              MMM      MMM    RRR   RR                VVV        RRR   RR
#
# My gitgub --> https://www.github.com/sharpvik <--
#



# functions 

## --> binary search
def binary(array, element):     # array(list) -- list of numbers; element(int / float) -- number you are searching for;
                                # --> function returns index of element if found, ohterwise returns -1;

    array.sort()                # sort the array just in case;

    low = 0                     # low(int) -- lowest searching limit;
    high = len(array) - 1       # high(int) -- highest searching limit;
    index = -1                  # index(int) -- index of the element if found, otherwise = -1;
    position = high // 2        # position(int) -- the index we're testing;
    
    while low < high:
        if element == array[position]:
            index = position
            return index
        elif element < array[position]:
            high = position - 1
        else:
            low = position + 1
        position = (high - low) // 2 + low
    else:
        if low == high and element == array[low]:
            index = low
        return index
## binary search <--



## --> linear search
def linear(array, element, count=1):    # array(list) -- any list; element(any type) -- element you are searching for; 
                                        # count(int) -- number of indexes saved before returning the answer;
    indexes = []
    i = 0

    while i < len(array) and len(indexes) < count:
        if array[i] == element:
            indexes.append(i)
        i += 1
        
    if len(indexes) == 0:
        return -1
    elif len(indexes) == 1:
        return indexes[0]
    else:
        return indexes
## linear search <--
