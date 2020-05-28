class Cat:

    def eat(self):
        print("%s 吃鱼" % (self.name))

    def drik(self):
        print("喝牛奶")

tom=Cat()
tom.name="Tom"
tom.eat()
lazyCat=Cat()
lazyCat.name="懒猫"
lazyCat.eat()
"""
self.用来访问对象的属性
self 调用其他的对象方法

"""