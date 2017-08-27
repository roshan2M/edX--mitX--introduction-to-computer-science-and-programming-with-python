# Lecture 6.3, slide 3

def removeDups(L1, L2):
    for e1 in L1:
        for e1 in L2:
            L1.remove(e1)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
removeDups(L1, L2) # Will yield L1 = [2, 3, 4]


def removeDupsBetter(L1, L2):
    L1Start = L1[:]
    for e1 in L1Start:
        for e1 in L2:
            L1.remove(e1)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
removeDupsBetter(L1, L2) # Will yield L1 = [2, 3, 4]