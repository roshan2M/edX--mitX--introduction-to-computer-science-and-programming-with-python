# Final Exam, Problem 4 - 1

def getSublists(L, n):
    '''
    Assumes L is not empty and n is an integer such that 0 < n <= len(L)
    Returns all possible sublists of L of length L without skipping elements in L
    '''
    sublists = []
    for i in range(len(L) - n + 1):
        sublists.append(L[i:i + n])
    return sublists