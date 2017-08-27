# Optional Problem Set, Question 1

def ndigits(x):
    '''
    assumes x is an integer
    returns the digits of x
    '''
    # If x equals 0 (due to integer division), it means that no digits are left.
    if x == 0:
        return 0
    # Otherwise, it returns 1 + the digits of the integer divided by 10.
    return 1 + ndigits(abs(x) / 10)