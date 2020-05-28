# Python解释器-1991年解释器的诞生，C语言实现，
# 变成机器语言，其他语言翻译成机器语言的工具，不同语言通过不同的编译器变成机器语言
# 编译器翻译有两种方式，1编译，2解释

# 编译型语言 C C++        解释性语言    Python
# 源代码                  源代码
# 编译器                  解释器- **********逐行解释每一句源代码
# 可执行文件
# 操作系统
# CPU
# 编译型语言是统一编译一次性执行，解释性语言是逐行解释每一句源代码
# 解释性语言速度慢
# 跨平台一次编写多个平台运行 解释性比较强，在不同的操作系统安装不同的解释器

# Python设计目标
# 简单直观，同样强大，开源，适应于短期开发的日常任务
# python解释器 Cpython-官方版本C语言实现，Jython-Java平台运行，IronPython可以在.Net和Mono平台运行
# PyPy python实现的
#
# 第一行注释
print("hello hello")
# 第二行注释
print("hello world")  # ssss
# 多行注释

"""
这是一个多行注释
。。。。
。。。
。
注释结束
"""
# print("-"*50)
# # a=2**3
# # print(a)
priceApple=float(input("请输入苹果的价格"))
weightApple=float(input("请输入苹果的重量"))
sumApple=priceApple*weightApple
print(sumApple)