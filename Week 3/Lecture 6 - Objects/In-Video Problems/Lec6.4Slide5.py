# Lecture 6.4, slide 5

def fact(n):
    '''
    assumes n is an integer
    returns n * (n - 1) * (n - 2) * ... * 1
    '''
    if n == 1:
        return n
    return n * fact(n - 1)

def fib(n):
    '''
    assumes n is an integer
    returns the nth term of the fibonacci sequence
    '''
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def applyFuns(L, x):
    '''
    assumes L is a list of functions
    assumes x is an integer
    returns each function in L applied to x
    '''
    for f in L:
        print(f(x))

applyFuns([abs, int, fact, fib], 4)