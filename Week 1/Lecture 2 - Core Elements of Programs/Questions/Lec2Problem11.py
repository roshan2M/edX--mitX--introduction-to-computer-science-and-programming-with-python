# Lecture 2, Problem 11

varA = "e"
varB = "g"

if (type(varA) == str or type(varB) == str):
    print ("string involved")
elif (varA > varB):
    print ("bigger")
elif (varA == varB):
    print ("equal")
elif (varA < varB):
    print ("smaller")