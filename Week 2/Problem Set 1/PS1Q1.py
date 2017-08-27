# Problem Set 1, Question 1
# Count the number of vowels in the string s.

s = 'abdcseeaedcae'

vowelCount = 0
for letter in s:
    if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
        vowelCount += 1

print ('Number of vowels: ' + str(vowelCount))