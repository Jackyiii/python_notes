"""
类名创建对象时，自动执行的操作
对象的内存中分配地址
创建对象
为对象的属性设置初始值-初始化方法
初始化方法使用是__init__----构造函数

"""
class Cat:
    def __init__(self,newName):
        self.name=newName
        self.age=""
        print("初始化方法，构造函数")
    def Eat(self):
        print("%s吃鱼"%self.name)
tom=Cat("Tom1")
# tom.name="Tom"
tom.Eat()

