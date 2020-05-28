class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("狗在叫")


class Houski(Dog):
    def bark(self):
        print("%s在叫" % (self.name))


class Over(Dog):
    def bark(self):
        print("%s在叫" % (self.name))


class Person:
    def __init__(self, name):
        self.name = name

    def dougouwan(self, dog):
        print("%s在逗%s" % (self.name, dog.name))
        dog.bark()


xiaoming = Person("阿福")
over = Over("over")
xiaoming.dougouwan(over)
