# Lecture 8.3, slide 4

def getRatios(v1, v2):
    '''
    assumes v1 and v2 are lists of equal length of numbers
    returns a list containing the meaning full values of v1[i] / v2[i]
    '''
    ratios = []
    if len(v1) != len(v2):
        raise ValueError('getRatios called with bad argument')
    for index in range(len(v1)):
        if (type(v1[index]) not in (int, float)) or (type(v2[index]) not in (int, float)):
            raise ValueError('getRatios called with bad argument')
        if v2[index] == 0.0:
            ratios.append(float('NaN')) # NaN = Not a Number
        else:
            ratios.append(float(v1[index] / v2[index]))
    return ratios