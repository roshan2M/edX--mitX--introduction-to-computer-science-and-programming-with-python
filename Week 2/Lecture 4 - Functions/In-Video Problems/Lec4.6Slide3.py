# Lecture 4.6, slide 3

# This function takes in x, power, and epsilon as arguments and returns x taken to the root of power within the range epsilon.
def findRoot1 (x, power, epsilon):
    '''
    x and epsilon int or float, power an int
        epsilon > 0 and power >= 1
    Returns a float y such that y ** power is within epsilon of x.
    If such a float does not exist, it returns None.
    '''
    # This says that if a negative number is being taken to an even root, then return None because it is not possible.
    if (x < 0 and power % 2 == 0):
        return None
    # Sets the low to the min of -1 and x.
    # Sets the high to the max of 1 and x.
    low = min(-1, x)
    high = max(1, x)
    # The initial answer is the average of the low and high.
    ans = (high + low) / 2.0
    # While the answer is not within epsilon, keep readjusting the values.
    while abs(ans ** power - x) > epsilon:
        if (ans ** power < x):
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans

print (findRoot1 (0.5, 2, 0.0001))