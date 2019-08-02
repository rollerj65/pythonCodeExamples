number = 1 + 2 * 3 / 4.0
#composite equation
print(number)


#Modulo
remainder = 11 % 3
print("Modulo operator")
print(remainder)


#power relationship
squared = 7 ** 2
cubed = 2 ** 3
print("Squared")
print(squared)

print("Cubed")
print(cubed)

#Using operators with strings
helloWorld = "hello" + " " + "world"
print("Operators with strings")
print(helloWorld)

#multiplying strings creates a repeating sequence
lotsOfHellos = "hello" * 10
print("String multiplication")
print(lotsOfHellos)

#Using Operators with Lists
#joining lists with addition operators
evenNumbers = [2,4,6,8]
oddNumbers = [1,3,5,7]
allNumbers = oddNumbers + evenNumbers
print("Adding evenNumbers string and oddNumbers string")
print(allNumbers)

#Creating a repeating sequence using multiplication
print("Create a repeating sequence of 1,2,3")
print([1,2,3] * 3)


#Exercise (Failed)
x = object()
y = object()

xList = [x] * 10
yList = [y] * 10
bigList = []

for x in xList:
    bigList.append(xList)

for y in yList:
    bigList.append(yList)


print("xList contains %d objects" % len(xList))
print("yList contains %d objects" % len(yList))
print("bigList contains %d objects" % len(bigList))

#testing code
if xList.count(x) == 10 and yList.count(y) == 10:
    print("Almost there...")
if bigList.count(x) == 10 and bigList.count(y) == 10:
    print("Great!")

print(bigList)

#Exercise (Succeeded)
x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")