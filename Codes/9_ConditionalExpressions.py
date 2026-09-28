# Conditional Expression = A one line shortcut for thr if-else statement (ternary operator)
#                          Print or assign one or two values based on a condition

#                          X if condition else Y

num = 5
a=6
b=7
age =25
print("Positive" if num > 0 else "Negative")
result = "Even" if num % 2 == 0 else "Odd"
max_num = a if a>b else b
min_num = a if a<b else b

status = "Adult" if age >=18 else "Child"

print(status)
print(max_num)
print(min_num)
print(result)