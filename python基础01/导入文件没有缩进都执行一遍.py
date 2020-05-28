
#文件被导入时，直接执行的代码不需要被执行
def sayHello():
    print("你好")
def main():
    print("主函数")
if __name__=="__main__":

    print("小明开发的模块")
    print(__name__)
    sayHello()
    main()
#__name__
#如果是被其他文件导入的，他就是模块名
#如果是当前执行的程序他就是__main__
