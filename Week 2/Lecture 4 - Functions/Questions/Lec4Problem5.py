# Lecture 4, Problem 5

# Defines a function called clip.
# This takes in 3 numbers, lo, x, and hi.
def clip (lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    # Here, this finds the minimum of all sets of values and finds the middle value.
    return max (min(lo, x), min(x, hi), min(lo, hi))

# This prints the value of some test cases.
print (clip(2,3,4))
print (clip(2,4,3))
print (clip(3,2,4))
print (clip(3,4,2))
print (clip(4,2,3))
print (clip(4,3,2))