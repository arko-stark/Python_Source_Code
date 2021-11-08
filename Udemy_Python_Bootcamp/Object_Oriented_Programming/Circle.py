class Circle():
    # class object attribute
    pi = 3.14
    def __init__(self, radius = 1):
        self.radius = radius
        # defining area as an attribute from the radius
        # class object attribute can be referred by the class name
        self.area = radius*radius*Circle.pi
    # method to get circumference
    def get_circumference(self):
        return self.radius*2*self.pi

# overriding default value of radius. the 30 can be omitted altogether
my_circle = Circle(30)
print(my_circle.get_circumference())
print(my_circle.area)
print(my_circle.pi)