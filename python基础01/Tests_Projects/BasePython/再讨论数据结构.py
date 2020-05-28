#list的特点是有序的  就是下标
#dict键不一定是数值了，有唯一的键 比较适合存储有复杂名称的数据
#将list转化为dict
a=[("key","value")]
b=dict(a)
print(b)
a=[("key","value"),(2,3),(2,5)]
b=dict(a)
#print(b)
a=[str(x)+"帅吗" for x in range(0,101)]
#print(a)

new_list=[]
for x in range(101):
    new_list.append(x)
#print(new_list)
#sorted(a,reverse=True)
#查看使用点击F1
#sorted方法需要赋值，sort不用
a=[(1,2,3),(3,4,5),(0,1,2)]
import operator
a.sort(key=operator.itemgetter(1,2))
print(a)
#三种字符串的拼接方法
#第一种方法
c="%s is a %s"%("a","b")
print(c)
#第二种方法
d="%(who)s is a %(gender)s" %{"who":"yi","gender":"boy"}
print(d)
#format
k="{who} is a {gender}".format(who="yi",gender="boy")
e="{} is a {}".format("i","girl")
print(k)
print(e)

