import math
friends = 5

# friends = friends + 1
# friends += 1

# friends = friends -2
# friends -= 2

# friends = friends*3
# friends *=3

# friends = friends/2
# friends /=2

# friends = friends **2
# friends **=2

# friends= friends%2
# friends %=2

print(friends)


# Maths
x = 3.14
y = -4
z = 5

# result = round(x) #round to the nearest number
# result = abs(y) # absoulute value is the distance away from zero as a whole number.
# result = pow(4, 3) #power function
# result = max(x, y, z)
result = min(x, y, z)

print(result)


x = 9.2

print(math.pi)
print(math.e)  # exponential constant
result = math.sqrt(x)
result = math.ceil(x)
result = math.flooe(x)
print(result)


# Circumference of Circle
radius = input('Enter the Radius of Circle:')
circumference = 2 * math.pi * radius
print(f"The Circumference is: {round(circumference, 2)}cm")


# Area of Circle
radius = float(input("Enter the radius of circle:"))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area, 2)} cm^2")


# Hypotenuse of Right Angle Triangle
a = float(input("Enter side A:"))
b = float(input("Enter side B:"))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")
