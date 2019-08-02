#Classes: template to build objects with

class myClass:
    variable = "foo"

    def function(self):
        print("This is a message inside the class.")
#multiple instances of the class can be declared at once.
myObjectX = myClass()
myObjectY = myClass()

#variables can be set outside the class
myObjectY.variable = "foo2"

#output both variables
print("myObjectX.variable: %s" % myObjectX.variable)
print("myObjectY.variable: %s" % myObjectY.variable)

#accessing functions in class
myObjectX.function()

#Exercise
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car2 = Vehicle()

car1.name = "Fer"
car1.kind = "Convertible"
car1.color = "red"
car1.value = 60000

car2.name = "Jump"
car2.kind = "Van"
car2.color = "blue"
car2.value = 10000


# test code
print(car1.description())
print(car2.description())
