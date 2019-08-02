#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
min = 1
max = 20

numbersToDivide = []
count = 0

#retrieve numbers to divide
for i in range (min, max + 1):
    count +=1
    numbersToDivide.append(i)

print(numbersToDivide)

canBeDivided = False
number = 1

while (canBeDivided == False):
    divideCheck = len(numbersToDivide)
    numberOfTimesDivided = 0
    for i in numbersToDivide:
        print("dividing %a by %s" % (number, i))
        if(number % i) == 0:
            numberOfTimesDivided +=1
    if (numberOfTimesDivided == divideCheck):
        canBeDivided = True
        print(number)
    number += 1

