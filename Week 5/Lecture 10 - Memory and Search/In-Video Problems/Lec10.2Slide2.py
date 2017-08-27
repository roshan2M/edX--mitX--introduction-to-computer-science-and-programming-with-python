# Lecture 10.2, slide 2

def search(L, e):
    # Goes through every element in the list.
    for i in range(len(L)):
        # If that element is equal to e, it returns True.
        if L(i) == e:
            return True
        # However, if it is greater than e, it must have surpassed its value, so it returns False.
        elif L(i) > e:
            return False
    # If none of the elements are greater than e and all of them have been checked, then it is not in the list.
    return False