
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

primeNumberList = []
primeNumberLimit = 10001


##
count = 0

while (len(primeNumberList) <= primeNumberLimit):
    
    prime = False
    
    for y in range(2, count):
        if(count % y) == 0:
            prime = False
            break
        else:
            prime = True
    if (prime == True):
        print("Adding %d to primeNumberList" % (count))
        primeNumberList.append(count)
    count += 1

print(primeNumberList)