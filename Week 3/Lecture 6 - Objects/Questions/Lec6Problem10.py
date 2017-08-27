# Lecture 6, Problem 10

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for i in range(len(aDict.values())):
        for j in aDict.values()[i]:
            count += 1
    return count

def howMany2(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for value in aDict.values():
        # Since all the values of aDict are lists, aDict.values() will be a list of lists.
        result += len(value)
    return result

def howMany3(aDict):
    '''
    Another way to solve the problem.
    aDict: A dictionary, where all the values are lists.
    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result