# Lecture 10.2, slide 4

def search(L, e):
    def bSearch(L, e, low, high):
        # If the high element is equal to the low element, the function just has to check if that element is e.
        if high == low:
            return L[low] == e
        # Otherwise, a midpoint is calculated and used to reference the search.
        mid = low + int((high - low) / 2)
        # Now, 3 cases are tested for in the function.
        # If the mid-element is e, then True is returned.
        if L[mid] == e:
            return True
        # If the mid-element is greater than e, then a binary search of the lower half of the list is returned.
        elif L[mid] > e:
            return bSearch(L, e, low, mid)
        # If the mid-element is less than e, then a binary search of the upper half of the list is returned.
        else:
            return bSearch(L, e, mid + 1, high)
    
    # In the main function, it is checked if the length of L is 0. If it is, e cannot be a member of L.
    if len(L) == 0:
        return False
    # Otherwise, a binary search of the entire list is conducted.
    else:
        return bSearch(L, e, 0, len(L) - 1)