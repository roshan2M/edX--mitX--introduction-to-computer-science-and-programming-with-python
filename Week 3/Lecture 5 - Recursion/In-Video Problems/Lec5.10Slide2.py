# Lecture 10, slide 2

def fibMetered(x):
    global numCalls
    numCalls += 1
    
    if x == 0 or x == 1:
        return 1
    return fibMetered(x - 1) + fibMetered(x - 2)

def testFib(n):
    for i in range(n + 1):
        global numCalls
        numCalls = 0
        print('Fibonacci of ' + str(i) + ' = ' + str(fibMetered(i)))
        print('Fibonacci called ' + str(numCalls) + ' times')