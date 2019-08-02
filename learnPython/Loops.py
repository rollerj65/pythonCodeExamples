
#for loop
primes = [2, 3, 5, 7]
print("for loop")
for prime in primes:
    print(prime)

print("print out 0, 1, 2, 3, 4")
for x in range(5):
    print(x)

print("print out 3, 4, 5")
for x in range(3, 6):
    print(x)

print("print out 3, 5, 7")
for x in range(3, 8, 2):
    print(x)

#while loops continue while condition is met.

print("while loop")
count = 0
while count < 5:
    print(count)
    count += 1

#break statements exit the loop when called
count = 0
print("break statement used")
while True:
    print(count)
    count += 1
    if count >= 5:
        break

#continue statements move onto the next loop

print("continue statement used")
for x in range(10):
    #check if x is even
    if x % 2 == 0:
        continue
    print(x)

#else statement
#if a break statement is used, then else is skipped
#if a continue statement is used, the else is executed

#print out 0, 1, 2, 3, 4 and then print "count value reached 5"
count = 0
print("")
while(count<5):
    print(count)
    count += 1
else:
    print("count value reached %d" % (count))

# if i is divisible by 5, print i
#if a break statement is used, then else is skipped
for i in range (1, 10):
    if (i%5 ==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

#Exercise
print("Print out all even numbers in the order they are received.")
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]
count = 0
for x in numbers:
    if (numbers[count] == 237):
        break
    else:
        if (numbers[count] % 2 == 0):
            print(numbers[count])             
    count += 1 


#Exercise solution code from website.
print("Solution from website.")
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    if number == 237:
        break

    if number % 2 == 1:
        continue

    print(number)