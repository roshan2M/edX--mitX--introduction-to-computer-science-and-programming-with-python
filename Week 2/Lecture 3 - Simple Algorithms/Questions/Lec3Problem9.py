# Lecture 3, Problem 9

# Asks the user to think of a number between 0 and 100.
print ('Please think of a number between 0 and 100!')

# Sets the initial low and high to 0 and 100, respectively.
low = 0
high = 100

# The answer is the average of the two, or 50.
# It then asks if the user's number is 50, and reads the user's response.
ans = (low + high) / 2
print ("Is your secret number " + str(ans) + "?")
response = str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))

# As long as the guess is incorrect, the following is output.
while (response != 'c'):
    # If the response is h, then the high is set to ans to decrease the ans later.
    if (response == 'h'):
        high = ans
    # If the response is l, then the low is set to ans to increase the ans later.
    elif (response == 'l'):
        low = ans
    # Otherwise, something wrong was typed.
    else:
        print ("Sorry, I did not understand your input.")
    
    # The answer is set to the average of the new high and low.
    ans = (low + high) / 2
    print ("Is your secret number " + str(ans) + "?")
    response = str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))

# When the correct number has been guessed, the game stops.
print ("Game over. Your secret number was: " + str(ans))