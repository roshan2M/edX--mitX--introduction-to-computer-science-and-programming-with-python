# Lecture 5, Problem 8

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    letter = len(aStr) / 2
    
    if aStr == '' or char == '':
        return False
    elif aStr.lower()[letter] == char.lower():
        return True
    elif len(aStr) == 1:
        return False
    elif aStr.lower()[letter] > char.lower():
        return isIn(char, aStr[:len(aStr) / 2])
    elif aStr.lower()[letter] < char:
        return isIn(char, aStr[len(aStr) / 2:])