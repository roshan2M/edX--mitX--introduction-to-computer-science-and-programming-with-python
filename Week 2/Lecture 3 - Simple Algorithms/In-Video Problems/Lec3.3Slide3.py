# Lecture 3.3, slide 3

x = int(raw_input('Enter an integer: '))

# Goes through each integer from 0 to abs(x) + 1 to see if any yield x.
for ans in range(0, abs(x) + 1):
    # If the cube of ans is x, then the program breaks.
    if (ans ** 3 == abs(x)):
        break

# If answer cubed is not equal to x even after for loop, then this is executed.
if (ans ** 3 != abs(x)):
    # Prints the appropriate statement.
    print (str(x) + ' is not a perfect cube.')

# If a perfect cube is found, the following code is executed.
else:
    # If x is less than 0, then the cube root must be negative.
    if (x < 0):
        ans *= -1
    # Prints the appropriate statement.
    print ('Cube root of ' + str(x) + ' is ' + str(ans))