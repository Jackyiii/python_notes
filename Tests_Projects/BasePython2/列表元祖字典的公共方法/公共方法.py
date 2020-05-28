"""
Python高级数据类型的内置函数 [] () {}
len(item)
del(item)
max(item)
min(item)
cmp(item1,item2) Python3取消了此函数

"""
a=[1,23,4]
del a[1]
print(a)
a.insert(1,24)
print(a)
del (a[1])
print(a)
a.insert(2,25)
print(max(a))
print(min(a))
#字典的是根据key进行统计
#字典和字典不能比较大小

#字典无法被切片
#字典无法用于*操作符因为key必须唯一
# +拼接会 出现新的列表 而 extend会在原有列表基础上加入

#成员运算符
# in     not in
print("a" in "abcde")
c = 'pythontab.com'
d = 'pythontab.com'
print(c is d)
"""
for 变量 in 集合:
    循环体代码
else:
    没有break退出循环，循环结束后，会执行的代码
通过break则不会else
"""
for a in [1,2,3]:
    print("执行")
else:
    print("会执行")
print("-"*20)
for b in[2,3,4]:
    if b==3:
        print("break")
        break
else:
    print("不会执行")

print("*"*40)
student=[
    {"name":"阿土"},
    {"name":"小妹"},
    {"name":"丹尼"}
]
findName="丹尼1"
for stu in student:
    if stu["name"]==findName:
        print("找到了%s"%(findName))
        break
else:
    print("没找到")
print("循环结束")
