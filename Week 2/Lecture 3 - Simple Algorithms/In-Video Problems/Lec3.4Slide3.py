# Lecture 3.4, slide 3

num = 222

# Checks if the number typed is positive or negative.
if (num < 0):
    isNeg = True
    num = abs(num)
else:
    isNeg = False

# The result is to referred as string. If num is 0, then the result is '0'.
result = ''
if (num == 0):
    result = '0'

# If the num is greater than 0, then the result equals the modulo of num.
# This value is concatenated with the result and the num is divided by 2.
while num > 0:
    result = str(num % 2) + result
    num = num / 2

# If the number is negative, then a negative sign is applied to the binary.
if (isNeg == True):
    result = '-' + result
    
print result