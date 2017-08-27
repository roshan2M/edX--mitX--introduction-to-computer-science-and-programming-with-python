# Lecture 3.4, slide 4

x = float(raw_input("Please enter an integer from 0 to 1: "))

# The following code says that as long as 2 to the pth power times x is not an integer, keep looking.
# When 2 ^ p * x is an integer, then it stops displaying the remainder.
p = 0
while (((2 ** p) * x) % 1 != 0):
    print ('Remainder = ' + str((2 ** p) * x - int((2 ** p) * x)))
    p += 1

# It then defines the number to be 2 ^ p * x, wherever p stops.
num = int ((2 ** p) * x)

# Sets the result to an empty string.
result = ''

# If the num is 0, then the result is also set to 0.
if (num == 0):
    result = '0'

# If num is greater than 0, the result is num % 2 added to the existing numbers that have been entered.
# Each time, num is divided by 2 to make sure that the next power of 2 is being evalutated.
while (num > 0):
    result = str(num % 2) + result
    num = num / 2

# It then joins 0 with the result.
for i in range(p - len(result)):
    result = '0' + result

# It then displays the final result.
result = result [0:-p] + '.' + result [-p:]
print ('The binary representation of the decimal ' + str(x) + ' is ' + str(result))