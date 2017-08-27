# Quiz, Problem 6

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    aNewList = []
    
    for elt in aList:
        if type(elt) == list:
            aNewList.extend(flatten(elt))
        else:
            aNewList.append(elt)
    
    return aNewList