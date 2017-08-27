# Lecture 12, Problem 5

def genPrimes():
    """
    Generates a list of prime numbers.
    """
    primes = []
    x = 1
    while True:
        x += 1
        for p in primes:
            if x % p == 0:
                break
        else:
            primes.append(x)
            yield x