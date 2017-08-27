# Problem Set 2, Question 1

# These hold the values of the balance, APR, monthly payment rate, and monthly interest.
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate / 12.0

# This captures the total paid value over the time period.
totalPaid = 0

# This goes through each month of the year.
for month in range(12):
    # This prints what month it is.
    print ("Month: " + str(month + 1))

    # This determines the minimum monthly payment, and adds it to the paid total.    
    minimumMonthlyPayment = monthlyPaymentRate * balance
    totalPaid += minimumMonthlyPayment
    print ("Minimum monthly payment: " + str(round(minimumMonthlyPayment, 2)))

    # This determines the unpaid balance that remains.
    monthlyUnpaidBalance = balance - minimumMonthlyPayment

    # This determines the balance that remains after minimum payment is made.
    balance = monthlyUnpaidBalance * (1 + monthlyInterestRate)
    print ("Remaining balance: " + str(round(balance, 2)))

# These print the total paid amount and the remaining balance after 1 year.
print ("Total paid: " + str(round(totalPaid, 2)))
print ("Remaining balance: " + str(round(balance, 2)))