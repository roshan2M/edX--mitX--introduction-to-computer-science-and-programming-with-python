# Lecture 6, slide 4

def findDivisors(n1, n2):
    '''
    assumes n1 and n2 are positive integers
    returns tuple containing common divisors of n1 and n2
    '''
    divisors = () # The empty tuple.
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            divisors += (i,)
    return divisors

divs = findDivisors(20, 100)
total = 0
for d in divs:
    total += d
print(total)