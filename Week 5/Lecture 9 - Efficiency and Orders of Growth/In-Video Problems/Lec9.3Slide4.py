# Lecture 9.3, slide 4

# This is an example of an algorithm of logarithmic complexity.

def intToStr(i):
    # Here is the list of all digits.
    digits = '0123456789'
    
    # If i simply is 0, then the corresponding string is returned.
    if i == 0:
        return '0'
    
    # Otherwise, a result variable is created to yield the string.
    result = ''
    
    # While i is positive, the result will be added to the remainder after division by 10.
    while i > 0:
        # The i % 10 will give the remainder after division by 10 - i.e. the last digit.
        result += digits[i % 10]
        # The value will be updated by division.
        i /= 10
    
    # The result will be returned.
    return result