# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER


#   List
fruits = ["apple", "orange", "banana", "coconut"]
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)
# fruits[0] = "pineapple"
fruits.append("pineapple")
fruits.insert(0, "pineapple")
print(fruits)
# for fruit in fruits:
    # print(fruit)


#   Set
fruits = {"apple", "orange", "banana", "coconut"}
fruits.add("pineapple")
fruits.remove("apple")
fruits.pop()

#Tuples
fruits = ("apple", "orange", "banana", "coconut")
print(len(fruits))