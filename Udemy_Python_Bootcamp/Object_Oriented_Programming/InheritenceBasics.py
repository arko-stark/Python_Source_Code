# defining the base class
class BaseAnimalClass():
    def __init__(self):
        print('Animal Created')
    def who_am_i(self):
        print('I am an animal')
    def eat(self):
        print('I eat meat')

myanimal = BaseAnimalClass()
print(myanimal.who_am_i())

# inheriting the Animal Class
class Dog(BaseAnimalClass):
    def __init__(self):
        BaseAnimalClass.__init__(self)
        print('I am a dog')
    # over-riding a method
    def who_am_i(self):
        print('I am a dog!!!')
    # adding a new method to the inherited class
    def bark(self):
        print('I can Woof !!!')

mydog = Dog()
mydog.who_am_i()
mydog.bark()
