# Lecture 4.3, slide 3
# Here, we are taking a number x and raising it to the power p via successive multiplication.

# The iterativePower method takes x and p as variables and finds x^p.
def iterativePower (x, p):
    result = 1 # Local variable to store temporary result.
    for i in range(p):
        print ('Iteration: ' + str(i) + '; Current: ' + str(result))
        result *= x # Result is multiplied by x each successive time.
    return result # Result is returned.