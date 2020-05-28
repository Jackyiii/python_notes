#用两种方法实现（5，2，3） a=（1，2，3）
a=(1,2,3)
b=list(a)
b[0]=5
a=tuple(b)
print(a)
#2
a=(1,2,3)
b=(5,)+a[1:3]
a=b
print("-----")
print(a)

#判断2是否在元祖里
print(dir(a))
b=list(a)
for i in b:
    if(i==2):
        print("存在")
    #else:
      #  print("不存在")

#集合a=set(['a','b','c'])做下面的操作

#添加字符串'jay'到集合a里面
a=set(['a','b','c'])
print(a)
a.add("jay")
print(a)


#集合b=set(['b','e','f','g'])用两种方法求集合a和集合b的并集
