# Lecture 9.3, slide 6

# This is an example of an algorithm of linear complexity.

def addDigits(s):
    # Assigns a running total.
    total = 0
    
    # Goes through each number in the string.
    for digit in s:
        # Adds to the running total.
        total += int(digit)
    
    # Returns the total.
    return total