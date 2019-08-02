
palindromeList = []


count = 0
while (count < 1000000):
    count +=1
    strCount = str(count)
    if strCount == strCount[::-1]:
        #print("matched!")
        palindromeList.append(str(count))
#retrieve list of palindromes
print(palindromeList)

number = 993399
factorsOfNumber = []

#find factors of number

for i in range (2, number):
    if(number % i) == 0:
            factorsOfNumber.append(i)

print(factorsOfNumber)

#code from https://stackoverflow.com/questions/12674389/highest-palindrome-with-3-digit-numbers-in-python
strCount = 0
for i in range(100,999):
    for j in range(100,999):
        multipliedValues = i*j
        if str(multipliedValues) == str(multipliedValues)[::-1]:
            if multipliedValues > strCount:
                strCount = multipliedValues
print(strCount)
