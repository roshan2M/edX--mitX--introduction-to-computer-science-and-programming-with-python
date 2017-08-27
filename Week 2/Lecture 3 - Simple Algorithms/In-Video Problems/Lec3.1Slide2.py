# Lecture 3.1, Slide 2

x = 2
ans = 0
itersLeft = x

# This code squares the value of x by repetitive addition.
while (itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft - 1
print (str(x) + ' * ' + str(x) + ' = ' + str(ans))