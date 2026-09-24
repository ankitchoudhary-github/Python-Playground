operator = input("Enter an Operator (+ - * /):")
num1 = float(input ("Enter the first number: "))
num2= float(input("Enter the second number:"))

if operator =="+":
    result = num1 + num2
    print (round(result))
elif operator =="-":
    result = num1 - num2
    print (round(result))
elif operator == "*":
    result = num1 * num2
    print (round(result))
elif operator == "/":
    result = num1 / num2
    print (round(result))
else:
    print(f"{operator} operator is not valid")