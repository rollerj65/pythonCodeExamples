
#Every function in Python receives a predefined number of arguments, if declared normally, like this:
def myFunction(first, second, third):
    ...

#variable number of arguments
def foo(first, second, third, *therest): #therest retrieves everything else
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest ... %s" % list(therest))

foo(1,2,3,4,5)

#send function arguments by keyword
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print(("the sum is: %d") % (first + second + third))

    if options.get("number") == "first":
        return first
result = bar(1,2,3, action = "sum", number = "first")
print("Result: %d" %(result))

#Exercise
# edit the functions prototype and implementation
def foo(a, b, c, *d):
    return(len(d))

def bar(a, b, c, **options):
    if options.get("magicnumber") == 7:
        return True
    if options.get("magicnumber") == 6:
        return False


# test code
if foo(1,2,3,4) == 1:
    print("Good.")
if foo(1,2,3,4,5) == 2:
    print("Better.")
if bar(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome!")

#solution
# edit the functions prototype and implementation
def foo(a, b, c, *args):
    return len(args)

def bar(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7


# test code
if foo(1,2,3,4) == 1:
    print("Good.")
if foo(1,2,3,4,5) == 2:
    print("Better.")
if bar(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome!")