# Lecture 6.4, slide 3

def applyToEach(L, f):
    '''
    assumes L is a list, f is a function
    mutates L by replacing each element, e in L, by f(e)
    '''
    for e in range(len(L)):
        L[e] = f(L[e])

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

L = [1, -2, 3.4]

# Takes the absolute value of each element in L.
applyToEach(L, abs)
print(L)

# Converts each element in L to an integer type.
applyToEach(L, int)
print(L)

# Takes the factorial of each element in L.
applyToEach(L, fact)
print(L)

# Finds the fibonacci sequence for each element in L.
applyToEach(L, fib)
print(L)