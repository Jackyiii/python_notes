#返回一个bool类型，元素在列表里返回true，否则返回false
#列表推导公示#[expr for iter_var in iterable ]
[x for x in range(1,11)]
range(1,11,1)
a=[33,11,22,44]
b=a.sort()
print(b)
if b is None: print("None")
print(a)
b=a.reverse()
print(a)
list=[1,2,3,4,5,333,11,44]
[x for x in list]
#print(x)
#range（起始位置，结束位置，步长）用于创建列表
for i in range(3,6,1):
    print(list[i])
    #第一种方法便利list
for i in list:
    print(i)
    #第二种方法遍历list
for i in range(len(list)):
    print(list[i])
    #第三种方法遍历list
    for i, val in enumerate(list):
        print (val)
for i,val in enumerate(list,2):
    print(val)
    #只是改变了起始序号

c1=[1,2,3]
c2=[4,5,6]
print(c1+c2)
c1.extend(c2)
print(c1)
d1=[1,99,33,44,55,22]
d1.insert(1,2)
d1.insert(7,(11,33,54))
print(d1)
del d1[7]
d1.insert(4,101)
print(d1)

a=[x for x in range(20,101) if x%2==0]
print(a)
#列表是可变的类型
b=[[1,2,3],[4,5,6]]
b[0][1]=8
print(b)
a=[1,2,3,4,4,5,6,7,8]
b=a[0:4:1]
print(b)
c=b[-1:-2:-1]
print(c)

