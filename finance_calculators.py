import math

# Below is the first thing the user will see when strting the program which gives then two choices,
# either an investment or bond calculator.
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
print("Enter either 'investment' or 'bond' from the menu above to proceed: ")
choice = input()
# Below is the first option (investment)
if choice == "investment":
    print("You have chosen the investment calculator.")
    deposit = float(input("Enter the deposit amount: "))
    rate = float(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of years you plan on investing: "))
    interest = input("Enter 'simple' or 'compound' interest: ")
# Here i ask the user if they would like simple or compound interest.
    if interest.lower() == "simple":
        total = deposit * (1 + (rate/100) * years)
    elif interest.lower() == "compound":
        total = deposit * pow((1 + (rate/100)), years)
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")
        total = 0

    print(f"Total investment amount: ${total:.2f}")
# Below is the second option (bond)
elif choice == "bond":
    print("You have chosen the home loan calculator.")
    house_price = float(input("Enter the house price: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    loan_period = int(input("Enter the loan period (in months): "))

    monthly_rate = interest_rate / 100 / 12

    monthly_payment = (monthly_rate * house_price)/(1 - (1 + monthly_rate)**(-loan_period))
 
    total_payment = monthly_payment * loan_period
    
    print(f"Monthly payment: ${monthly_payment:.2f}")
    print(f"Total payment: ${total_payment:.2f}")
#Below is the else statement linked to the first if statement. 
else:
    print("Invalid choice. Please enter investment or bond.")


  
