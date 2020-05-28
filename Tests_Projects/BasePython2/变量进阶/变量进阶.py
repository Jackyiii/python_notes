#不可变类型，数字，字符串，bool float complex long 元祖--》地址固定了
#可变类型：列表和字典-》内存中的数据可以被修改 -》修改内存地址中的内容需要通过方法例如append remove等方法进行修改
a=[1,2,3]
print(id(a))
a.append(1)
print(id(a))
a=[1,2,3,1]
print(id(a))
print("*"*15)
d=[
    {"name":"yi"},
    {"age":1}
]
print(id(d))
print(id(d[0]["name"]))
d[0].clear()
print(d)
d.clear()
print(d)
print(id(d))
#字典的key是不可变类型
print("-"*100)
a=hash(1)
print(a)
b=hash("hello")
print(b)
c=hash((1,))
print(c)
