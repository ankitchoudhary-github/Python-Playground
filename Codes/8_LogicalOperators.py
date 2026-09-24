# Logical Operators = Evaluate Multiple conditions (or, and, not)
#                   or = atleast one condition is true
#                   and = both cnoditions must be True
#                   not = inverts the condition (not False, not True)

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")





temp = -5
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is Sunny")

elif temp <= 0 and is_sunny:
    print("It is cold outside")
    print("It is Sunny")

elif 28> temp >0 and is_sunny:
    print("It is Warm outside")
    print("It is Sunny")





temp = -5
is_sunny = True

if temp >= 28 and not is_sunny:
    print("It is hot outside")
    print("It is Cloudy")

elif temp <= 0 and not is_sunny:
    print("It is cold outside")
    print("It is Cloudy")

elif 28> temp >0 and not is_sunny:
    print("It is Warm outside")
    print("It is Cloudy")
