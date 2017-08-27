# Lecture 2.6, slide 4

x = int(raw_input('Enter an integer: '))
if (x % 2 == 0):
    if (x % 3 == 0):
        print ('Divisible by 2 and 3.')
    else:
        print ('Divisible by 2 but not 3.')
elif (x % 3 == 0):
    print ('Divisible by 3 but not 2.')