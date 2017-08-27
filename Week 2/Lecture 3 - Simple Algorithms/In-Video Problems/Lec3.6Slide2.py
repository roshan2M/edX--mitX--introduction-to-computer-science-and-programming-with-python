# Lecture 3.6, slide 2

# Defines the value to take the square root of, epsilon, and the number of guesses.
x = 9
epsilon = 0.01
numGuesses = 0

# Here, 0 < x < 1, then the low is x and the high is 1 - the sqrt(x) > x if 0 < x < 1.
# If x > 1, then the low is 0 and the high is x - the sqrt(x) < x if x > 1.
if (x >= 0 and x < 1):
    low = x
    high = 1.0
elif (x >= 1):
    low = 0.0
    high = x

# Sets the initial answer to the average of low and high.
ans = (low + high) / 2.0

# While the answer is still not close enough to epsilon, continue searching.
while (abs(ans ** 2 - x) >= epsilon):
    # For each case, it prints the low and high values.
    print ('low = ' + str(low) + ' ; high = ' + str(high) + ' ; ans = ' + str(ans))
    numGuesses += 1
    
    # If the guess is lower than x, then set the new ans = low.
    # If the guess is higher than x, then set the new ans = high.
    if (ans ** 2) < x:
        low = ans
    elif (ans ** 2) >= x:
        high = ans
    
    # At the end, the answer is updated.
    ans = (low + high) / 2.0

# Prints the number of guesses and the final guess.
print ('Number of guesses taken: ' + str(numGuesses))
print (str(ans) + ' is close to the squre root of ' + str(x))