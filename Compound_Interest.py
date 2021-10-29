# Here is Python Program To Calculate Compound Interest

P = int(input("Principle Amount: ")) # The Initial Amount You Borrowed or deposited
r = float(input("Enter Annual Rate of Interest: ")) # r = 1/100
n = int(input("Enter number of times that interest is compounded in a year: "))
t = float(input("Enter number of years the amount is deposited or borrowed for: "))
Total_Balance = P * ( 1 +(r/n))**(n * t)  # // Total Amount Accumulated After
                                          # n years, including interest //

print("Total Balance After no of Years: " + str(Total_Balance))

