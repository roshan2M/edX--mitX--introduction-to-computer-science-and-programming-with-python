# Lecture 5.5, slide 2

def iterFact (n):
    '''
    assumes that n is an int > 0
    returns n!
    '''
    result = 1
    while (n > 0):
        result *= n
        n -= 1
    return result

def recurFact (n):
    '''
    assumes that n is an int > 0
    returns n!
    '''
    if (n == 1):
        return n
    return n * recurFact (n - 1)