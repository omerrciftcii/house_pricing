'''numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

count = 0

for number in numbers:
    if(number % 2 == 1):
        continue
    if(number == 237):
        break
    print(number)
'''

'''def list_benefits():
    X=["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
    return X

def build_sentence(info):
    sentence = info + "is a benefit of functions!"
    return sentence

print(list_benefits())
print(build_sentence("Reliable"))
'''

                                # CLASS AND OBJECTS IN PYTHON

class MyClass:
    variable = "Yeah"

    def functioın(self):
        print("This is a message inside the class ")


myobject = MyClass()
myobject.functioın()
myobject. variable


#EXAMPLE: We have a class defined for vehicles.
# Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth $60,000.00 with a name of Fer,
#  and car2 to be a blue van named Jump worth $10,000.00.

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

 




