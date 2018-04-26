def factorial(n):
    if n > 1:
        return factorial(n - 1) * n
    else:
        return 1

def nPr(n, r):
    return int(factorial(n) / factorial(n - r))

def nCr(n, r):
    return int(factorial(n) / ( factorial(n - r) * factorial(r) ))
