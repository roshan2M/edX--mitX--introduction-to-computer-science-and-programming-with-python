# Lecture 3.5, slide 2

# This code finds the square root of real numbers to 2 decimal places.

x = 25
epsilon = 0.01
stepSize = epsilon ** 2
numGuesses = 0
ans = 0.0

# Keeps looping while the difference between ans^2 and x is greater than the epsilon and the answer is less than x.
# Each time, the answer is increased by the step size and numGuesses by 1.
while (abs(ans ** 2 - x) >= epsilon and ans <= x):
    ans += stepSize
    numGuesses += 1

# Prints the number of guesses taken.
print ('Number of guesses taken: ' + str(numGuesses))

# If it could not find the square root, prints a certain message.
# Otherwise, prints the value of the square root found.
if (abs(ans ** 2 - x) >= epsilon):
    print ('Could not find the square root of ' + str(x))
else:
    print ('The square root of ' + str(x) + ' is ' + str(ans))