
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.


primeNumberList = []
primeNumberLimit = 2000000
sumPrimeNumbers = 2

##
count = 1
rangeLimit = 10

while (count <= primeNumberLimit):
    
    prime = False
    
    for y in range(2, count):
        if(count % y) == 0:
            prime = False
            break
        else:
            prime = True
    if (prime == True):
        print("Adding %d to primeNumberSum" % (count))
        sumPrimeNumbers += count
    count += 1

print(sumPrimeNumbers)
