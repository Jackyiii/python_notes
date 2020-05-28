#元祖是有序的集合
#通过偏移位置来获取数据
#属于不可变对象，不能原地修改内容，没有排序
#元祖不可变的好处在于保证了数据的安全确保不会改变我们的数据从而导致程序的问题
a=(1,2,3,4,5,6,7)
print(a[0])
print(a[5:7])#切片[起始位置不包括，取到的位置包括]
print(dir(a))
#若想修改元祖的值，首先要转换成list
#a[0]=4无法修改tuple的值
b=list(a)
b[0]=5
print(type(b))
a=tuple(b)
print(a)
#集合没有顺序，无法使用切片索引进行操作
#集合分为，可变集合，set()不可变集合frozenset()
#添加操作：add update
#删除remove
#成员关系in not in
#交集并集差集
#set去重列表内容元素重复
a=set()#列表，元祖，字典，字符串可迭代的对象 __iter__对象的内置方法可以迭代，返回可迭代的对象
b=set('abc')
print(b)
print(type(b))
b.add("acdde")
print(b)
b.update("python")
print(b)#每个元素进行插入
b.remove("acdde")
print(b)
c1=set("abcdef")
c2=set("bj")
print(c1& c2)
print(c1|c2)
print(a-b)#在a中出现不在b
#去除重复
a=[1,2,3]
a.append(1)
a.append(3)
print(a)
s=set(a)
print(s)
a=list(s)
print(a)
a=frozenset("a","b","c")
#a.add("l")
#a.remove("a")
#报错不可变

print(a)

