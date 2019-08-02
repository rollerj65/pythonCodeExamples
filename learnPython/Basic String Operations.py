
aString = "Hello world!"
aString2 = "Hello world!"

#single quotes need to be stored in a ""
print ("single quotes are ''")
#return length of aString
print("Length of aString")
print(len(aString))

#index of "o" in aString
print("index of 'o' in aString")
print(aString.index("o"))

#count number of "l" in aString
print("number of 'l' characters in aString")
print(aString.count("l"))

#print part of the string. [startingindex:endingindex]
#[onenumber] retrieves character at index. [:3] retrieves everything 
#before index 3. [3:] retrieves everything past index 3.
# negative indexes are used to start at the end of a string. [-3] = 3rd from last character.
print("print aString starting at index 3, and ending at index 6")
print(aString[3:7])

print("print aString characters past index 3")
print(aString[3:])

print("print aString characters before index 3")
print(aString[:3])

##print part of string, and skip character [startingindex:endingindex:characterstoskip]
#form: [start:stop:step]
print("print aString characters between indexes 3 and 6")
print(aString[3:7])

print("print aString characters between indexes 3 and 6, while skipping 1 character")
print(aString[3:7:1])

#reverse?
print("reverse aString")
print(aString[::-1])

#set aString to upper-case
print("set aString to upper-case")
print(aString.upper())

#set aString to lower-case
print("set aString to lower-class")
print(aString.lower())

#startswith() and endswith() check if string starts or ends with the input
print("check if aString starts with 'hello'")
print(aString.startswith("Hello"))

print("check if aString ends with 'world'")
print(aString.endswith("foobar"))

#split creates divides the string into pieces based on the input
print("split aString into two strings.")
aFewWords = aString.split(" ")
print(aFewWords)

#Exercise:

s = "stre thera! ha home?"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))








