# Lecture 10.1, slide 3

def search(L, e):
    # Goes through every element in L.
    for i in range(len(L)):
        
        # If the element in the list matches the element, True is returned.
        if L[i] == e:
            return True
    
    # Otherwise, False is returned.
    return False