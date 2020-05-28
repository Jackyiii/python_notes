class Person:
    def __init__(self, _name, _weight):
        self.name = _name
        self.weight = _weight

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1

    def __str__(self):
        return "%s的对象，体重是%.1f"%(self.name,self.weight)
xiaoming = Person("小明", 120)
xiaoming.run()
xiaoming.eat()
xiaoming.eat()
print(xiaoming)