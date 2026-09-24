unit = input("Is this temperature in Celcius or Farenheit (C/F):")
temp = input("Enter the temperature:")

if unit == "C":
    temp = round((9*temp/5+32, 1))
    print(f"The Temperature in Farenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp-32*5/9, 1))
    print(f"The Temperature in Celcius is: {temp}°C")
else:
    print(f"{unit} is invalid unit of measurement")
