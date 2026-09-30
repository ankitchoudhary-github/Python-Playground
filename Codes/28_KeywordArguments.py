# Keyword Arguments
# A keyword argument is an argument passed to a function using the parameter name.
# Keyword arguments improve readability and make function calls more flexible.
# The order of keyword arguments does not matter.

# Order of arguments:
# 1. Positional
# 2. Default
# 3. Keyword
# 4. Arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")


hello("Hello", title="Mr.", first="Ankit", last="Choudhary")


# for loop print 1 to 10
for x in range(1, 11):
    print(x, end=" ")  # end is actually a keyword argument


# Phone
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"


phone_num = get_phone(country=1, area=123, first=456, last=7890)

print(phone_num)
