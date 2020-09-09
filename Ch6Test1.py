import math
def select_menu():
    print("Menu")
    print("1. circle 2. rectangle 3. triangle 4. Exit")
    menu=input("please choose : ")
    return(menu)

def cal_circle(radius):
    area=math.pi*radius*radius
    return(area)

def cal_rectangle(width,hight):
    area=width*height
    return(area)

def cal_triangle(base,height):
    area=1/2*base*height
    return(area)

print("Program calculate area.")
while True:
    menu=select_menu()
    if menu=="1":
        radius=int(input("Enter rasius : "))
        print("Area of circle = ",cal_circle(radius))
    elif menu=="2":
        width=int(input("Enter width : "))
        height=int(input("Enter height : "))
        print("Area of rectangle = ",cal_rectangle(width,height))
    elif menu=="3":
        base=int(input("Enter base : "))
        height=int(input("Enter height : "))
        print("Area of triangle = ",cal_triangle(base,height))
    elif menu=="4":
        break
    else:
        print("Menu input Error, enter again.")

print("Exit Program...")
