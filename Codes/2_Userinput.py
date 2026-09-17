# input() = A function that prompts the user to enter data
#           returns the netered data as a string

name= input("What is your name?:")
age= input("How old are you?:")

age= int(age)
age= age+1

print(f"You are {age} years old and your name is {name}")


# Excercise 1 => Area of Rectangle Calculation
length= float(input("Enter the length of the rectangle:"))
breadth= float(input("Enter the breadth of the rectangle:"))

Area= length*breadth

print(f"Area of Rectangle is {Area} cm²") #command for superscript is num on alt+0178


#Exercise 2 => Shopping Cart Problem
item = input("What item you would like to buy?: ")
price= float(input("What is the price?"))
quantity = int(input("How many would you like?:"))

total = price * quantity

print(f"You have brought {quantity} x {item}/s")
print(f"Your total is: {total}")