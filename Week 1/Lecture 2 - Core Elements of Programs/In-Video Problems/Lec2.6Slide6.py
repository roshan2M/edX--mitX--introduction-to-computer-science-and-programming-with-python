# Lecture 2.6, slide 6

x = int(raw_input('Enter an integer: ')) # Asks the user for a number x.
y = int(raw_input('Enter an integer: ')) # Asks the user for a number y.
z = int(raw_input('Enter an integer: ')) # Asks the user for a number z.

if (x < y and x < z):
    print ('x is least')
elif (y < z):
    print ('y is least')
else:
    print ('z is least')