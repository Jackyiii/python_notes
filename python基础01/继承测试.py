class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")

class Dog(Animal):
    def braik(self):
        print("叫")

wangcai=Dog()
wangcai.eat()
wangcai.braik()