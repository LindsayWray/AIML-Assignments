"""
Tom is a money lender and lends money to many people based on compound
interest. It has become very hectic for him to calculate the interest and total
amount. Can we help him by writing a program that could calculate the interest and
amount when details like principal amount, rate of interest and number of years?
Example output: Enter the principal: 1000
Enter rate of interest: 5%
Enter No. of years: 2
Amount = 1102.5
C.I. = 102.5
"""

principal = float(input("Enter the principal: "))
interest = input("Enter rate of interest: ")
years = int(input("Enter No. of years: "))
interest = int(interest.split("%")[0])
amount = principal * ((interest / 100) + 1)**years
print(f"Amount = {round(amount, 2)}\nC.I.= {round(amount - principal, 2)}")
