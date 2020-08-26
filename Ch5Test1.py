Done=True
while Done:
    D=input("Enter integer number(0-exit) : ")
    if D!="0":
        E=D[0]
        for n in D:
            if E<n:
                E=n
        print(f"Maximum Digit of integer number : {D} = {E}")
    elif D=="0":
        Done=False
print("Exit Program")
