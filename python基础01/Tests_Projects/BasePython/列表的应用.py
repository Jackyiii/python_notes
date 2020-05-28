from pip._vendor.urllib3.connectionpool import xrange

a="axd"
b=list(a)
print(b)
#返回列表
#tuple与list区别是@ 元祖不可变，list可变
#元祖大小固定，list的数据可以动态变化
#tuple用于存储异构数据，当作没有字段名的记录使用，比如tuople来记录一个人的身高体重和年龄
#person("zhang",3,30)
#point(x,y)坐标
#list一般用于存放同构数据
#["a","lisi","wang"]
#数据库操作中查询出来的记录都使用元祖组成的列表结构
#[("zhang",30,3),("li",20,1)("qing",2,3)]
#相对元祖不可变所以大小差异元祖比较小速度快
a=list((1,2))
print(a)
#传入元祖顺序也是一样的
#list(12)会报错，因为数字是不可迭代的对象

#xrange和range区别
# xrange(开始，结束，步长）它生成一个xrange的对象
a=xrange(1,10)
print(a)
b=range(1,11)
print(b)
print(a[0])
print(b[0])
#range方法是直接生成一个列表对象
#xrange的方法是生成一个xrange对象-生成器
#当我们需要操作非常的数据的时候，而且内存比较吃紧我们可以用xrange进行节省内存#
#当我们一般用在循环里面，比如我们只需要操作部分数据的话，而不是返回所有数据的话，推荐使用xrange

#取所有值的平方
a=[x*x for x in range(100)]
print(a)
#生成字符串
b=["this is %s"% x for x in range(3)]
print(b)
c=[(x,y) for x in range(2) for y in range(3)]
print(c)
x=dict(c)
print(x)
#列表的引用
a=["O","am","K"]
b=2
b=a
print(b)
print(id(b))
print(id(a))
a[2]="k"
print(a)
del b
print(a)
#del a删除引用
#del a[:]清空列表的元素
del a[:]
print(a)