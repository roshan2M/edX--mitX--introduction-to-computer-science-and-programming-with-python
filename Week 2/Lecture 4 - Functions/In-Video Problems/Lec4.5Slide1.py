# Lecture 4.5, slide 1

# Defines a function 'square' that takes the square of x.
def square(x):
    return x * x

# Defines a function 'twoPower' that provides a quick way of raising x to a power of n that is divisble by 2.
def twoPower(x, n):
    while (n > 1):
        x = square (x)
        n = n / 2
    return x

# Defines some initial conditions and calls the functions to see how the variables respond.
x = 5
n = 1
print (twoPower(2,8))