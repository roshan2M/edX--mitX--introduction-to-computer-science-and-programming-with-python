# Problem Set 2, Question 2

# These hold the values of the balance.
balance = 1000
origBalance = balance

# These hold the values of the annual and monthly interest rates.
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0

lowestPayment = 0

# This goes through all the possibilites.
while (balance > 0):
    # Adds 10 to the lowest payment and resets the balance.
    lowestPayment += 10
    balance = origBalance
    
    # This goes through each month of the year.
    for month in range(12):
        # This determines the balance that remains after payment is made.
        balance = (balance - lowestPayment) * (1 + monthlyInterestRate)

print ("Lowest Payment: " + str(lowestPayment))