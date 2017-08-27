# Quiz, Problem 5

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    result = 0
    for i in range(len(listA)):
        result += listA[i] * listB[i]
    return result