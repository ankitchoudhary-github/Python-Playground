# Typecasting - the process of converting a variable from one data type to another
#               str(), int(), bool()

name= "ANkit"
age= 25
gpa = 5.0
is_student= True

print(type(name))

gpa= int(gpa)
print(f"Our GPA is {gpa}")

age= float(age)
print(age)

#str
age= str(age)
age +="1"
print(age)

#bool
name = bool(name)
print(name)