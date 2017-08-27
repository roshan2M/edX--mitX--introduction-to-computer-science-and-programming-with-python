# Problem Set 1, Question 2
# Print the number of times the string 'bob' occurs in string s.

s = 'abdadbobakcbebob'

bobCount = 0
for num in range(len(s)):
    if (s [num:num + 3] == 'bob'):
        bobCount += 1

print ('Number of times bob occurs is: ' + str(bobCount))