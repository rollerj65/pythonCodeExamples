#function declaration
def myFunction():
    print("Hello world")

#function with arguments
def myFunctionWithArgs(username, greeting):
    print("Hello %s , From My Function!, I with you %s" % (username, greeting))

#function that returns values
def sumTwoNumbers(a,b):
    return a + b

def listBenefits():
    outputString = ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
    return outputString

def buildSentence(info):
    return info + " is a benefit of functions"

def name_the_benefits_of_functions():
    list_of_benefits = listBenefits()
    for benefit in list_of_benefits:
        print(buildSentence(benefit))

print("simple greeting")
myFunction()

#return more complicated greeting
print("More complicated greeting")
myFunctionWithArgs("John Doe", "a great year!")


#function with return
print("sum 1 and 2 to equal 3")
sumTwoNumbers(1,2)

name_the_benefits_of_functions()


#Solution from site:
# Modify this function to return a list of strings as defined above
#def list_benefits():
#    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

## Modify this function to concatenate to each benefit - " is a benefit of functions!"
#def build_sentence(benefit):
#    return "%s is a benefit of functions!" % benefit


#def name_the_benefits_of_functions():
#    list_of_benefits = list_benefits()
#    for benefit in list_of_benefits:
#        print(build_sentence(benefit))

#name_the_benefits_of_functions()