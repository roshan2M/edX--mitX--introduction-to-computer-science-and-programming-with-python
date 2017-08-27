# Lecture 6, Problem 5

aList = range(1, 6)
bList = aList
aList[2] = 'hello'
print(aList == bList)

cList = range(6, 1, -1)
dList = []
for num in cList:
    dList.append(num)