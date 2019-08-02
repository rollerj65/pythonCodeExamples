#In this exercise, you will need to print an alphabetically sorted list of all functions in the re module, which contain the word find.
import re

functionList = [dir(re)]
#print(functionList)
functionListSplit = str(functionList).split(",")
print(functionListSplit)
for functionDir in functionListSplit:
    strFunction = functionDir
    if ( (str(strFunction).find("find") > -1 )):
       print("found find: %s" % strFunction)
       ...
    else:
        #functionList.remove(strFunction)
        ...
#print(functionList)