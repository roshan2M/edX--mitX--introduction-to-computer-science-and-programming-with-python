# Lecture 4.1, slide 2

# This function returns the maximum of two numbers, x and y.
def max (x, y):
    # It retuns x if x is larger than y and vice versa.
    if (x > y):
        return x
    else:
        return y

# Finds the "max" of 3 and 4, and prints the answer.
z = max (3, 4)
print (str(z))