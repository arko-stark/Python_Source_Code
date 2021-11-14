class Dog():
    # attributes defined at class object
    # same for any instance of a class
    species = 'mammal'
    def __init__(self,breed,name,spots):
        # Attributes
        # we take in the argument
        # assign it using self.attribute_name
        self.breed = breed
        self.name = name
        # this is a boolean True/False
        self.spots = spots
    # OPERATIONS/ACTIONS ---- > METHODS
    def bark(self, number):
        print(f'My dog whose name is {self.name} barks and the number is {number}')

#create instance of the class
my_dog = Dog(breed = 'Lab', name = 'Gampu', spots=False)

# calling an atribute does not require paranthesis
print(my_dog.species)


# calling a method requires paranthesis
my_dog.bark(10)