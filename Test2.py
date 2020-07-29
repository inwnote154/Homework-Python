# นาย นวพรรษ นกงาม 6306021620018 Sec 1RA

amount=float(input("Enter amount : "))
rate=float(input("Enter rate : "))/100
year=float(input("Enter year : "))

FV=amount*(1+rate)**year
print("Future value =",round(FV,2))

print("\n")
print("Future value 1-10 years")
amount=amount*(1+rate)
print("Future value 1 years =",round(amount,2))
amount=amount*(1+rate)
print("Future value 2 years =",round(amount,2))
amount=amount*(1+rate)
print("Future value 3 years =",round(amount,2))
amount=amount*(1+rate)
print("Future value 4 years =",round(amount,2))
amount=amount*(1+rate)
print("Future value 5 years =",round(amount,2))
amount=amount*(1+rate)
print("Future value 6 years =",round(amount,2))
amount=amount*(1+rate)
print("Future value 7 years =",round(amount,2))
amount=amount*(1+rate)
print("Future value 8 years =",round(amount,2))
amount=amount*(1+rate)
print("Future value 9 years =",round(amount,2))
amount=amount*(1+rate)
print("Future value 10 years =",round(amount,2))

