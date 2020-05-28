class Cat:
    def eat(self):
        print("小猫爱吃鱼")
    def drink(self):
        print("小猫和水")
"""
创建猫对象

"""
tom=Cat()
tom.drink()
tom.eat()

lazyCat=Cat()
print(tom)
print(lazyCat)
addr=id(tom)
addr2=id(lazyCat)
print("%d"%addr)
print("%d"%addr2)
"""
%x 16进制
%d 10进制
"""