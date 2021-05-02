# inheritance

class Animal():
    def __init__(self):
        print('Animal created')
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print('I am eating')


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)  # creating instance of class Animal()
        print('dog created')
    def who_am_i(self):        # methods inside class
        print('I am a dog')    # class getting called 
    def bark(self):            # takes priority
        print('Woof!!!')       

my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()

# polymorphism

class Dog():
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(self.name + "Woof!!!")


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + "Nya~!!!")


kuro = Dog('kuro')
shiro = Cat('shiro')

kuro.speak()
shiro.speak()