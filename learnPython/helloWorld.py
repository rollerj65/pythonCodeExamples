#Training used: LearnPython.org
#Hello world + variables

print("hello world")


fruits = ["1", "2", "3", "4", "5"]
for x in fruits:
    print(x)
    
x = 1
if x == 1:
    #standard indentation is 4 spaces
    print("x is 1")

print("goodbye world")

#Integer
myInt = 20
print (myInt)

#Float
myFloat = 7.111
print(myFloat)
myFloat = float(7)
print(myFloat)

#String
myString = "Hello"
print(myString)
myString = 'Hello'
print(myString)

#Use "" where you can
myString = "Don't worry about apostrophes when using double quotes"
print(myString)

#Simple operators
#adding integers
one = 1
two = 2
three = one + two
print(three)

#adding strings
hello = "hello"
world = "world"
helloWorld = hello + world
print(helloWorld)

#declaring more than one variable per line
three, four = 3, 4
print(three, four)

#mixing int and strings don't work
#one = 1
#two = 2
#hello = "hello"
#print(one + two + hello)

myInt = 20
myFloat = 10.0
myString = "Hello"

#variable comparison
if myString == "Hello":
    print("String: %s" % myString)
if isinstance(myFloat, float) and myFloat == 10.0:
    print("Float: %f" % myFloat)
if isinstance(myInt, int) and myInt == 20:
    print("Int: %d" % myInt)

