# Lecture 8.4, slide 2

def getSubjectStats(subject, weights):
    '''
    gets the subject statistics for the student's grades
    '''
    return [[elt[0], elt[1], avg(elt[1], weights)]
            for elt in subject]

def avg(grades, weights):
    '''
    assumes grades and weights are lists of equal length and are not empty
    returns the weighted average of the assignments
    '''
    assert not len(grades) == 0, 'no grades data'
    assert len(grades) == len(weights), 'wrong number of grades'
    newGrades = [convertLetterGrade(elt) for elt in grades]
    result = dotProduct(newGrades, weights) / len(grades)
    assert 0.0 <= result <= 100.0, 'invalid average'
    return result

def convertLetterGrade(grade):
    '''
    converts a letter grade into a number grade
    if grade is already a number, then number is returned
    '''
    if type(grade) == int:
        return grade
    elif grade.upper() == 'A':
        return 90.0
    elif grade.upper() == 'B':
        return 80.0
    elif grade.upper() == 'C':
        return 70.0
    elif grade.upper() == 'D':
        return 60.0
    else:
        return 50.0

def dotProduct(a,b):
    '''
    returns the product of each grade and each weight to calculate the total
    '''    
    result = 0.0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result