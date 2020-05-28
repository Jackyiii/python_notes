"""
如果不需要访问类属性和实例属性
就可以将方法变成静态方法
@statement
def 静态方法（）

"""
class Dog:
    @staticmethod
    def run():
        print("跑的静态方法")
# dog1=Dog()
# dog1.run()
Dog.run()