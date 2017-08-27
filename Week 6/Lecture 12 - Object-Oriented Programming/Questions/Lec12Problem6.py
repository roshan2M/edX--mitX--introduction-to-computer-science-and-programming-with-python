# Lecture 12, Problem 6

def genPrimesFn():
    '''
    Function to return 1000000 prime numbers.
    '''
    primes = []   # primes generated so far
    last = 1      # last number tried
    while len(primes) < 1000000:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
    return primes

def genPrimesFn2():
    '''
    Function to print every 10th prime 
    number, until you've printed 20 of them.
    '''
    primes = []   # primes generated so far
    last = 1      # last number tried
    counter = 1
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            counter += 1
            if counter % 10 == 0:
                # Print every 10th prime
                print last
            if counter % (20*10) == 0:
                # Quit when we've printed the 10th prime 20 times (ie we've
                # printed the 200th prime)
                return



def genPrimesFn3():
    '''
    Function to keep printing the prime number until the user stops the program.
    This way uses user input; you can also just run an infinite loop (while True)
    that the user can quit out of by hitting control-c
    '''
    primes = []   # primes generated so far
    last = 1      # last number tried
    uinp = 'y'    # Assume we want to at least print the first prime...
    while uinp != 'n':
        last += 1
        for p in primes:
            if last % p == 0:
                break
            else:
                primes.append(last)
                print last
                uinp = raw_input("Print the next prime? [y/n] ")
                while uinp != 'y' and uinp != 'n':
                    while uinp:
                        print "Sorry, I did not understand your input. Please enter 'y' for yes, or 'n' for no."
                        uinp = raw_input("Print the next prime? [y/n] ")
                if uinp == 'n':
                    break