#def是关键词，括号冒号，永不忘，无缩紧无真相
#没有return的函数不是大丈夫，不是真函数
#不写doc函数，就像没有性别的人类

#函数的参数方法和陷阱
#如何定义参数
#参数的位置和可选参数
#参数的值是局部变量
#参数只在函数的内部有用
#全局变量的介绍
#使用方法
#全局变量最讨厌
#函数的默认值
#如何修改参数
#介绍
#**是字典，*是元祖
#def(define):
#函数很重要

#coding=utf-8
# def test():
#     " 这里写入文档 "
#     a="422"
#     return a
# print(test())
# print (test.__doc__)
# def test2(a,b,c,d):
#     "文档"
#     return a,b,c,d
# print(test2(1,2,3,4))
# print (test2.__doc__)
# def test3(a=1):
#     "可变参"
#     return a
# print(test3())
# print(test3(a=5))
# def test4(a,b,c,d,return_data="json"):
#     if return_data=="json":
#         return json(a,b,c,d)
#     elif return_data=="xml":
#         return xml(a,b,c,d)
#     return a,b,c,d
# test4(1,2,3,4,return_data="xml")
# b=4
# def a():
#     global b
#     b=5
#     return b
# print(a())
# b=[1,2,3,4]
# def func(l):
#     l.append(5)
#     return l
# b=func(b)
# print(b)
def test5(**kr):
    return kr
print(test5(a=1,b=3,c=5))
def test6(*tuple,**kr):
    return tuple,kr
print(test6(1,2,3,4,5,[1,2,3],a=1,b=2))


