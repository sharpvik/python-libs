def _not(x):        # x(int / str) -- any binary input (only 0s and 1s)

    return "".join([ ('1' if i == '0' else '0') for i in str(x) ])

def _and(x, y):     # x(int / str) and y(int / str) -- any binary input (only 0s and 1s)

    x, y = str(x), str(y)
    return "".join( [ ('1' if x[i] == y[i] == '1' else '0') for i in range( len(x) ) ] )

def _or(x, y):      # x(int / str) and y(int / str) -- any binary input (only 0s and 1s)

    x, y = str(x), str(y)
    return "".join( [ ('1' if x[i] == '1' or y[i] == '1' else '0') for i in range( len(x) ) ] )

def _xor(x, y):     # x(int / str) and y(int / str) -- any binary input (only 0s and 1s)

    x, y = str(x), str(y)
    return "".join([ ('1' if x[i] != y[i] else '0') for i in range( len(x) ) ])
