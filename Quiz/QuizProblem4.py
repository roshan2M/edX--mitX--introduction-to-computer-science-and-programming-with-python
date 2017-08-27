# Quiz, Problem 4

def isPalindrome(aString):
    '''
    aString: a string
    '''
    for i in range(len(aString)):
        if aString.lower()[i] != aString.lower()[len(aString) - i - 1]:
            return False
    return True