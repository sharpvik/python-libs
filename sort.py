#
# ================================         BBBBBB      YY    YYY           MMMM    MMMM    RRRRRR              VV      VVV    RRRRRR
# =             THE              =         BBB   BB     YY  YYY            MMMMM  MMMMM    RRR   RR             VV    VVV     RRR   RR
# ===> Sort functions library <===         BBBBBB        YYYYY             MMM  MM  MMM    RRRRRR                VV  VVV      RRRRRR
# =         (25.04.2018)         =         BBB   BBB      YYY              MMM      MMM    RRR  R                 VVVVV       RRR  R
# ================================         BBBBBBBB       YYY              MMM      MMM    RRR   RR                VVV        RRR   RR
#
# My gitgub --> https://www.github.com/sharpvik <--
#



# functions

## --> insertion sort
def insertion(array):                                   # array(list) -- unsorted list of numbers; --> function returns a sorted list of numbers
    def insert(initial_position, array, position):
        array[position + 1:] = array[position:]
        array[position] = array[initial_position + 1]
        array.pop(initial_position + 1)

    for a in range(1, len(array)):
        for b in range(0, a):
            if b == 0 and array[a] <= array[b]:
                insert(a, array, b)
                break
            elif array[a] > array[b] and array[a] <= array[b + 1]:
                if b + 1 != a:
                    insert(a, array, b + 1)
                break
    return array
## insertion sort <--



## --> merge sort
def merge_arrays(left, right):                      # *** internal use ***
    output = []

    while len(left) != 0 or len(right) != 0:
        try:    
            left_minimum = left[0]
            right_minimum = right[0]
            if left_minimum < right_minimum:
                output.append(left_minimum)
                left.pop(0)
            else:
                output.append(right_minimum)
                right.pop(0)
        except IndexError:
            if len(left) == 0:
                for each in right:
                    output.append(each)
                break
            else:
                for each in left:
                    output.append(each)
                break

    return output

def merge(array):                                   # array(list) -- unsorted list of numbers; --> function returns a sorted list of numbers
    if len(array) == 1:
        return array
    else:
        middle = len(array) // 2
        left_half = array[:middle]
        right_half = array[middle:]
        return merge_arrays(merge(left_half), merge(right_half))
## merge sort <--
