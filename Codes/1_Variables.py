# Variable = A container for a value (string, integer, float, boolean)
#   A Variable behaves as if it was the value it contains

# Strings
first_name = "Bro"
food = "pizza"
email = "123@fake.com"
print(f"Hello {first_name}")  # f-string= formatted string literals
print(f"You like {food}")
print(f"Your email is {email}")

# Integers
age = 23
quantity = 3
number_of_students = 30

print(f"Let's say you're {age} years old")
print(f"You are buying {quantity} items")
print(
    f"Your class has {number_of_students} students with an average of {age} years")

# Float - A number containing decimal portion
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your GPA is: {gpa}")
print(f"You ran for {distance} kms")

# Boolean - True or False
is_student = True
for_sale = False

if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")
