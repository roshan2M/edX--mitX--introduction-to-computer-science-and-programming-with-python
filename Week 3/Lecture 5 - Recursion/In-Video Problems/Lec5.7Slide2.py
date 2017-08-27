# Lecture 5.7, slide 2

def fibonacci(x):
    '''
    assumes x is an int >= 0
    returns xth term of the fibonacci sequence
    '''
    assert type (x) == intern and x >= 0
    if x == 0 or x == 1:
        return 1
    return fibonacci(x - 1) + fibonacci(x - 2)