
#A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. Each value stored in a dictionary can be accessed using a key, 
#which is any type of object (a string, a number, a list, etc.) instead of using its index to address it.

#declaring dictionary variables manually
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print("phonebook without brackets: %s" % phonebook)

#declaring dictionary variables in brackets
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print("phonebook with brackets: %s" % phonebook)

#declaring dictionary on one line
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}

#iterating through dictionary
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

#removing a value
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}

del phonebook["John"]
print("phonebook without John: %s" % phonebook)

#using phonebook.pop instead
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
phonebook.pop("John")
print("phonebook without John: %s" % phonebook)


#Exercise
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here
phonebook.update({"Jake" : 938273443 })
phonebook.pop("Jill")

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")