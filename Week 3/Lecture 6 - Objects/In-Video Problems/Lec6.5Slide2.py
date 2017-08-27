# Lecture 6.5, slide 2

monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 1:'Jan', 2:'Feb', 3:'Mar'}
print(monthNumbers['Jan'])
print(monthNumbers[2])

monthNumbers['Apr'] = 4
monthNumbers[4] = 'Apr'
print(monthNumbers)
print(monthNumbers[4])

collect = []
for e in monthNumbers:
    collect.append(e)

print(collect)

myDict = {(1, 2):'twelve', (1, 3):'thirteen'}
print(myDict[(1, 2)])