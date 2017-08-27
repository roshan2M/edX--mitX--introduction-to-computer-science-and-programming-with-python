# Lecture 9.1, slide 5

def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False