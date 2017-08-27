# Lecture 9.3, slide 7

# This is another example of an algorithm of linear complexity.

def factorial(n):
    # If n is 1, it returns the base value 1.
    if n == 1:
        return 1
    
    # Otherwise, it returns the product of n and the factorial of n - 1.
    return n * factorial(n - 1)