# Lecture 3.7, slide 3

# The epsilon defines how close the guess must be to y for the guess to be acceptable.
# y is the number entered by the user.
# guess is the guess for the square root of y.
epsilon = 0.01
y = 24.0
guess = y/2.0

# While the difference between guess squared and y >= 0.01, the program keeps generating guesses.
while (abs(guess ** 2 - y) >= epsilon):
    guess = guess - (((guess ** 2) - y) / (2 * guess))

# It finally prints the square root of y found.
print ('Square root of ' + str(y) + ' is about ' + str(guess))