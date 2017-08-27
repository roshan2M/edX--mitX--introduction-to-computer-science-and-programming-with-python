# Problem Set 2, Question 3

# These hold the values of the balance.
balance = 320000
origBalance = balance

# These hold the values of the annual and monthly interest rates.
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12

lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12.0

# This goes through all the possibilites.
while (abs(balance) > 0.01):
    # Reset the value of balance to its original value
    balance = origBalance
    # Calculate a new monthly payment value from the bounds
    payment = (upperBound - lowerBound) / 2 + lowerBound

    # Test if this payment value is sufficient to pay off the entire balance in 12 months
    for month in range(12):
        balance -= payment
        balance *= 1 + monthlyInterestRate

    # Reset bounds based on the final value of balance
    if balance > 0:
        # If the balance is too big, need higher payment so we increase the lower bound
        lowerBound = payment
    else:
        # If the balance is too small, we need a lower payment, so we decrease the upper bound
        upperBound = payment

print ("Lowest Payment: " + str(round(payment, 2)))