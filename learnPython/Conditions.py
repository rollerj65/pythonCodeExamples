
#booleans are used to evaluate conditions
x = 2
print("x == 2")
print(x == 2)

print("x == 3")
print(x == 3)

print("x < 3")
print(x < 3)

# "and" or "or" operators work the same
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

#python uses indentation to define code blocks, instead of brackets
#objects that are empty are considered true
#example empty values: 1) an empty string: "" 2) an empty list: [] 
#3) The number zero 4) the false boolean: False

#Example from site
#if <statement is="" true="">:
#    <do something="">
#    ....
#    ....
#elif <another statement="" is="" true="">: # else if
#    <do something="" else="">
#    ....
#    ....
#else:
#    <do another="" thing="">
#    ....
#    ....
#</do></do></another></do></statement>

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal two.")

# 'is' operator does not match values of the variables. Instead it matches the instances.

x = [1,2,3]
y = [1,2,3]
print("compare values using '=='")
print(x == y)

print("compare instances using 'is'")
print(x is y)

# 'not' operator acts as normal
print("not false")
print(not False)

print("false")
print((not False) == (False))

#Exercise
#change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

#website solution
#change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")