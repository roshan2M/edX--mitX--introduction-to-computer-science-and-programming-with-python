# Lecture 7.7, slide 4

def isPal(x):
    assert type(x) == list
    temp = x[:]
    '''
    # Print statement for debugging
    print(temp, x)
    '''
    # temp.reverse - Not invoking the method, just accessing it.
    temp.reverse()
    '''
    # Print statement for debugging.
    print(temp, x)
    '''
    if temp == x:
        return True
    else:
        return False

def silly(n):
    result = []
    for i in range(n):
        '''
        # Initial, buggy position of initialization of result.
        result = []
        '''
        elem = raw_input('Enter element: ')
        result.append(elem)
        '''
        # Print statement for debugging.
        print(result)
        '''
    '''
    # Print statement for debugging.
    print(result)
    '''
    if isPal(result):
        print('Yes')
    else:
        print('No')