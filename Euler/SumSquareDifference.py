

#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
import math
maxNumber = 100
sumSquare = 0
sumOfNumbers = 0
squareOfSum = 0
sumSquareDifference = 0

#calculate sum of squares for 1 to maxNumber
for i in range(1, maxNumber + 1):
    multipliedValue = (math.pow(i,2))
    print(multipliedValue)
    sumSquare += multipliedValue

print(sumSquare)

#calculate square of the sum
count = 1
for x in range (1, maxNumber + 1):
    print(count)
    sumOfNumbers += count
    count += 1

squareOfSum = (sumOfNumbers*sumOfNumbers)



sumSquareDifference = squareOfSum - sumSquare
print("squareOfSum: %d, sumSquare: %d, sumSquareDifference: %d " % (squareOfSum, sumSquare, sumSquareDifference))