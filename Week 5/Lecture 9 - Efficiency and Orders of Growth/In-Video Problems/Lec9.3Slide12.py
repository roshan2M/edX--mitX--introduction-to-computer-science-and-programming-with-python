# Lecture 9.3, slide 12

# This is another example of an algorithm of quadratic complexity.

def intersect(L1, L2):
    # Creates a temporary list.
    temp = []
    
    # Goes through each element in L1.
    for e1 in L1:
        
        # Goes through each element in L2.
        for e2 in L2:
            
            # If they are the same the element is added.
            if e1 == e2:
                temp.append(e1)
    
    # To remove the duplicates the result list is created.
    result = []
    
    # Goes through every element in temp.
    for e in temp:
        
        # If the element is not already in result, then it is added to result.
        if e not in result:
            result.append(e)
    
    # Result is returned.
    return result