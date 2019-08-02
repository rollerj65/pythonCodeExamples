#%s - String (or any object with a string representation, like numbers)

#%d - Integers

#%f - Floating point numbers

#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

#%x/%X - Integers in hex representation (lowercase/uppercase)


# Using a variable in a string
name = "John"
print("Hello, %s" % name)

#using multiple arguments
name = "John"
age = 23
print("%s is %d years old." % (name, age))

#variables can be converted to string using %s
myList = [1,2,3]
print("A list: %s" % myList)

#Exercise
data = ("John", "Doe", 53.44)
firstName = data[0]
lastName = data[1]
cost = data[2]

formatString = "Hello"

print("%s %s %s. Your current balance is %.2f." % (formatString, firstName, lastName, cost))


#Solution from site
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

