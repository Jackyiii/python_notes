class Person:
    def __init__(self,name):
        self.name=name
        self.__age=18
    def __secret(self):
        print("%s年龄是%d"%(self.name,self.__age))

xiaofang=Person("小芳")
xiaofang._Person__secret()