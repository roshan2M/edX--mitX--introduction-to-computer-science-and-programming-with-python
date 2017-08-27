# Lecture 9.3, slide 10

# This is an example of an algorithm of quadratic complexity.

def isSubset(L1, L2):
    # Goes through every element in L1.
    for e1 in L1:
        
        # Lets matched equal False to begin with.
        matched = False
        
        # Then goes through every element in L2.
        for e2 in L2:
            
            # If the two elements are equal, then matched is true and the loop is broken out of.
            if e1 == e2:
                matched = True
                break
        
        # If, after the loop, the elements don't match, then False is returned.
        if matched == False:
            return False
    
    # If all tests have been passed, then True is returned.
    return True