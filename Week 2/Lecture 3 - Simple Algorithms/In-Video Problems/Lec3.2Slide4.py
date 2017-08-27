# Lecture 3.2, slide 4

x = int(raw_input('Enter an integer: '))
ans = 0

# Checks if the cube of the answer is less than x.
while (ans ** 3 < x):
    ans += 1
    
# If answer cubed does not equal x, then x is not a perfect cube.
if (ans ** 3 != x):
    print (str(x) + ' is not a perfect cube.')

# Otherwise, it is a perfect cube.
else:
    print ('Cube root of ' + str(x) + ' is ' + str(ans) + '.')