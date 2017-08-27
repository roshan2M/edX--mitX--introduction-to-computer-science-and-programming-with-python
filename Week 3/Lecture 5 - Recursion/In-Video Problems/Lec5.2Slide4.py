# Lecture 5.2, slide 4

'''
This function calculates the multiplication of 2 numbers via successive addition.
Parameter a: the initial value
Parameter b: the number of times the initial value should be added to itself
Return iterMult: the successive addition of a by b times via recursion
'''

def recurMult (a, b):
    if (b == 1):
        return a
    return a + recurMult (a, b - 1)