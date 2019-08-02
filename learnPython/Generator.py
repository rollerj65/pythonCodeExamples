#Generators: special iterator function that returns a iterable set, one at a time, in a special way
#generators are very easy to implement, but a bit difficult to understand.
#Generators are used to create iterators, but with a different approach. Generators are simple functions which return an iterable set of items, one at a time, in a special way.
#When an iteration over a set of item starts using the for statement, the generator is run. Once the generator's function code reaches a "yield" statement, the generator yields its execution back to the for loop, returning a new value from the set. The generator function can generate as many values (possibly infinite) as it wants, yielding each one in its turn.
#Here is a simple example of a generator function which returns 7 random integers:

#EXAMPLE
import random

def lottery():
    #returns 6 number between 1 and 40
    for i in range(6):
        yield random.randint(1,40)

    #returns a 7th number between 1 and 15
    yield random.randint(1,15)

for randomNumber in lottery():
    print("And the next number is... %d!" % (randomNumber))


# SOLUTION from site fill in this function
def fib():
    a = 1
    b = 1
    while 1:
        yield a
        a, b=b, a + b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break