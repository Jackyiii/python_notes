class Animal:
    def jiao(self):
        print("动物")
class Dog(Animal):
    def jiao(self):
        super().jiao()
        print("狗")
xtq=Dog()
xtq.jiao()