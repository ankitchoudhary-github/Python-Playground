# Default Arguments
# A default argument is a parameter that has a default value.
# The default value is used when no value is provided for that argument.
# Default arguments make functions more flexible and reduce the number of arguments required.

# Types of Arguments:
# 1. Positional Arguments
# 2. Default Arguments
# 3. Keyword Arguments
# 4. Arbitrary Arguments


import time


def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1-discount) * (1+tax)


print(net_price(500))


# Timer

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")


count(30,15)
