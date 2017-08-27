# Lecture 5.1, slide 3

'''
This function calculates the multiplication of 2 numbers via successive addition.
Parameter a: the initial value
Parameter b: the number of times the initial value should be added to itself
Return iterMult: the successive addition of a by b times
'''

def iterMult (a, b):
    result = 0
    while (b > 0):
        result += a
        b -= 1
    return result