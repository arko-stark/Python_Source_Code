class Dog():
    def __init__(self,breed,name,spots):
        # Attributes
        # we take in the argument
        # assign it using self.attribute_name
        self.breed = breed
        self.name = name
        # this is a boolean True/False
        self.spots = spots

#create instance of the class
my_dog = Dog(breed = 'Lab', name = 'Gampu', spots=False)
print(my_dog.name)