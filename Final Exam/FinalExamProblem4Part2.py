# Final Exam, Problem 4 - 2

def longestRun(L):
    '''
    Assumes L is a non-empty list
    Returns the length of the longest monotonically increasing
    '''
    maxRun = 0
    tempRun = 0
    for i in range(len(L) - 1):
        if L[i + 1] >= L[i]:
            tempRun += 1
            if tempRun > maxRun:
                maxRun = tempRun
        else:
            tempRun = 0
    return maxRun + 1