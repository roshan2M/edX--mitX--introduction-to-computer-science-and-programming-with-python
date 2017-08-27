# Lecture 10.3, slide 3

def selectionSort(L):
    # Goes through every element in the list.
    for i in range(len(L) - 1):
        # Assigns the element the value of the minimum as seen so far.
        minIndex = i
        minValue = L[i]
        # From the next element and onward, it checks to see what is the smallest value.
        j = i + 1
        while j < len(L):
            # If a smaller value than L[i] is found, then L[j] replaces it.
            if minValue > L[j]:
                minIndex = j
                minValue = L[j]
            j += 1
        # This simply stores the value of the last element in the position of j so that it can be sorted later.
        temp = L[i]
        L[i] = L[minIndex]
        L[minIndex] = temp
    # This returns the list L.
    return L