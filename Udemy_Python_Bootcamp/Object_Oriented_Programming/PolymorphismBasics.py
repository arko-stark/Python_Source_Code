class Dog():
    def __int__(self, name) :
        self.name = name
    def speak(self):
        return self.name + ' Says Woof!'
class Cat():
    def __int__(self, name) :
        self.name = name
    def speak(self):
        return self.name + ' Says Meaow!'

# create instance of the classes
niko = Dog("Niko")
felix = Cat("Felix")
print (niko.speak())
print(felix.speak())