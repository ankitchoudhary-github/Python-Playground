#Nested loop = A nested loop is simply a loop inside another loop.
#   Outer loop → runs first
#       Inner loop → runs completely for every iteration of the outer loop

for x in range(3):
    for y in range(1,10):
        print(y, end="")
    print()


#Program to calculate Number of rows and columns in a rectangle
rows = int(input("ENter the # of rows: "))
columns= int(input("Enter the #of Columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()