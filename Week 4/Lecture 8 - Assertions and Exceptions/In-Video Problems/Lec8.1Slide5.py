# Lecture 8.1, slide 5

def divide(x, y):
    '''
    assumes x and y are ints/floats and y != 0
    raises exception for division by 0
    raises exception for incorrect types
    returns x / y
    '''
    try:
        result = x / y
    except ZeroDivisionError,e:
        print("Division by zero! " + str(e))
    except TypeError:
        divide(int(x), int(y))
    else:
        print("Result is: " + str(result))
    finally:
        print("Executing finally clause.")