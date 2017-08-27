# Quiz, Problem 7

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    interDict = {}
    diffDict = {}
    
    for key1 in d1.keys():
        if key1 in d2.keys():
            interDict[key1] = f(d1[key1], d2[key1])
        else:
            diffDict[key1] = d1[key1]
    
    for key2 in d2.keys():
        if key2 in d1.keys():
            interDict[key2] = f(d1[key2], d2[key2])
        else:
            diffDict[key2] = d2[key2]
    
    result = (interDict, diffDict)
    
    return result

def f(a, b):
    return a + b