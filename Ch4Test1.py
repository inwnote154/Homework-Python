num=str(input('Enter integer number(4 digit) : '))
num1=num[0]
num2=num[1]
num3=num[2]
num4=num[3]
n=num1

if n<num1:
    n=num1
elif n<num2:
    n=num2
elif n<num3:
    n=num3
elif n>num4:
    n=num4
else:
    print()

print(f"Maximum Digit of integer number {num} = {n}")
