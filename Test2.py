amount=float(input("Enter amount : "))
rate=float(input("Enter rate : "))
rate=float(rate/100)
year=float(input("Enter year : "))

FV=amount*(1+rate)**year
print("Future value =",FV)
