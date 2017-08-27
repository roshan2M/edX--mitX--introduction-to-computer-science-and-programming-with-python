# Lecture 7.3, slide 3

def sqrt(x, eps):
    '''
    assumes x and eps are floats
    x >= 0, eps > 0
    returns result such that
    x - eps < result * result < x + eps
    '''