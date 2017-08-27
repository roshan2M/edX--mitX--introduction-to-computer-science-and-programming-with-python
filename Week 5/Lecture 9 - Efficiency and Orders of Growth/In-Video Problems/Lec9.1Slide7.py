# Lecture 9.1, slide 7

def factorial(n):
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer