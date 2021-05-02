# Object oriented programming
# we create a 'class' and then we define it depending on our needs

class Dog():
    kingdom = 'mammal'
    def __init__(self, name, breed): # it is similar to contructors in c++ or java 
        self.name = name
        self.breed = breed
    # function inside a class is called method 
    def bark(self, age):
        print('woof! my name is {} and i am {} years old'.format(self.name, age))


my_dog = Dog('kuro','lab')

my_dog.bark(3)

class Circle():
    # Class object attribute
    pi = 3.14
    def __init__(self, radius = 1):
        self.radius = radius
        self.area = radius*radius*Circle.pi        # we can also use self.pi
    def get_circumference(self):                   # but Circle.pi is more 
        return self.radius * self.pi * 2           # readable

my_circle = Circle(10)
print(my_circle.pi)
print(my_circle.get_circumference())

