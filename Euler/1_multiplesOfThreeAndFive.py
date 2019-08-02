
#Multiples of 3 and 5
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
sumOfMultiples = 0
multiples = []
count = 0

while count < (1000):
    if (count % 3 == 0 or count % 5 == 0):
        multiples.append(count)
        sumOfMultiples += count
        print(sumOfMultiples)
    count += 1


