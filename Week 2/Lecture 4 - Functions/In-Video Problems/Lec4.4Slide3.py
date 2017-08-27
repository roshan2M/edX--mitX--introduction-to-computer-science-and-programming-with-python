# Lecture 4.4, slide 3

# Defines a function f that has a formal parameter x.
def f(x):
    y = 1 # Sets a local variable y equal to 1.
    x += y # Assigns x to x + y or x + 1, in this case.
    print ('x = ' + str(x)) # Prints what x equals to.
    return x # Returns the value of x to the global environment.

x = 3
y = 2
z = f(x) # Calls the function f at x or 3, in this case.