# Lecture 9.1, slide 10

def sqrtBi(x, eps):
    low = 0.0
    high = max(1, x)
    ans = (high + low) / 2.0
    while abs(ans ** 2 - x) >= eps:
        if ans ** 2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans