# Lecture 4.3, slide 1
# Here, we are taking a number x and raising it to the power p via successive multiplication.

# Takes the values of the base and exponent from the user.
x = float(raw_input('Enter a number: '))
p = int(raw_input('Enter an integer power: '))

# Sets an intermediate result variable to find the result.
result = 1

# Gives the result every time an iteration is completed.
for i in range(p):
    result *= x
    print ('Iteration: ' + str(i + 1) + '; Current Result: ' + str(result))