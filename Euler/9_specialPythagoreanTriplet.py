
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

range2 = 10000
product = 0

for c in range(1, range2):
    for b in range(1, c):
        #print("comparing b: %d to c: %d" % (b, c))
        for a in range(1, b):
           #print("comparing a: %d to b: %d" % (a, b))
            if((a*a) + (b*b) == (c*c)):
                print("found pythagorean triplet a: %d, b: %d, c: %d" % (a,b,c))
                if(a+b+c == 1000):
                    product = a*b*c
                    print("a: %d, b: %d, c: %d, product: %d" % (a,b,c,product))
                    break
        if (product > 1):
            break
    if (product > 1):
            break
