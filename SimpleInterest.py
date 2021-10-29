# Welcome To Python 
# Here is The Python Program to Calculate Simple Interest


P = int(input("Enter Total Money Want to Borrow or Invest: "))
r = float(input("Enter Annual Rate of Interest: "))
t = int(input("Enter Time in Years For Borrow or Invest: "))
simple_interest = P * r * t /100

print(" Total simple interest after no of years is Rs: " + str(simple_interest))
