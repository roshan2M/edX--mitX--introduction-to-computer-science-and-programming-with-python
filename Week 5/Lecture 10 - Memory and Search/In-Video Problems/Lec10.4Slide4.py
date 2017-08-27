# Lecture 10.4, slide 4

def merge(left, right):
    result = [] # Will contain final list.
    i, j = 0, 0 # Counters for left list and right list.
    while i < len(left) and j < len(right):
        # Checks if the first element in the left list is bigger and appends that element.
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        # Otherwise, it appends the first element in the right list.
        else:
            result.append(right[j])
            j += 1
    # If there are any elements left in the left list, it appends those to result.
    while i < len(left):
        result.append(left[i])
        i += 1
    # If there are any elements left in the right list, it appends those to result.
    while j < len(right):
        result.append(right[j])
        j += 1
    # Returns the final result of merging the two lists.
    return result

def mergeSort(L):
    # If the length of the list is 0 or 1, then it has already been sorted.
    if len(L) < 2:
        return L[:]
    # Otherwise, it sorts the elements in the list.
    else:
        # A mid-point is defined in the list.
        middle = int(len(L) / 2)
        # A left and right list are defined as the left and right halves of the list.
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        # The merge sort of those lists is returned.
        return merge(left, right)