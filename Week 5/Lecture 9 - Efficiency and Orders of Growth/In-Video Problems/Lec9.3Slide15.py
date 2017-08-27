# Lecture 9.3, slide 15

# This is an example of an algorithm of exponential complexity.

def genSubsets(L):
    # If the list is empty, an empty list of lists is also returned.
    if len(L) == 0:
        return [[]]
    
    # Get all the subsets without the last element.
    smaller = genSubsets(L[:-1])
    
    # Get all the subsets just of the last element.
    extra = genSubsets(L[-1:])
    
    # Creates a new list to store more subsets.
    new = []
    
    # For each element in smaller, it is appended to small plus the last element.
    for small in smaller:
        new.append(small + extra)
    
    # Combine those with the last element and those without the last element.
    return smaller + new