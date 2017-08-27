# Lecture 9.1, slide 9

def sqrtExhaust(x, eps):
    step = eps ** 2
    ans = 0.0
    while abs(ans ** 2 - x) >= eps and ans <= max(x, 1):
        ans += step
    return ans