#While loop = execute some condition while some condition remains true

#1
name= input("Enter your name:   ")

while name == "":
    print("You didnt enetered your name")
    name= input("Enter your name:   ")
print(f"Hello{name}")


#2
food = input("ENter a food you like (q to quit):")
while not food=="q":
    print(f"You like food")
    food = input("ENter a food you like (q to quit):")
print("Bye")


#3
num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"Your number is {num}")