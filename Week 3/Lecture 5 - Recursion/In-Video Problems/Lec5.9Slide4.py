# Lecture 5.9, slide 4

def isPalindrome(s):
    
    def toChars(s):
        s = s.lower()
        ans = ""
        for letter in s:
            if letter in 'abcdefghijklmnopqrstuvwxyz':
                ans += letter
        return ans
    
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

print (isPalindrome ('AbCdeDcBa'))
print (isPalindrome (''))
print (isPalindrome ('Able'))