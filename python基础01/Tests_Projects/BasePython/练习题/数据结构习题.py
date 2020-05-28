#a=[11,22,24,2,30,32]
#1把28插入列表末端、
a=[11,22,24,29,30,32]
#a.insert(,28)insert是插入因此不是最后一个，需要使用 append
a.append(28)
print(a)
#2在29后面插入57
a.insert(4,57)
print(a)
#3把11修改成6
a[0]=6
print(a)
#删除元素32
a.remove(32)
print(a)
#列表从小到达排序
a.sort()
print(a)
#----------------------------
#列表b=[1,2,3,4,5]
#两种方法输入[1,2,3,4,5,6,7,8]
b=[1,2,3,4,5]
c=[6,7,8]
a=b+c
print(a)
b=[1,2,3,4,5]
c=[6,7,8]
b.extend(c)
print(b)
#两种方法返回结果[5,4]
b=[1,2,3,4,5]
b.reverse()
b.remove(3)
b.remove(2)
b.remove(1)
print(b)
c=[1,2,3,4,5]
d=[c[4],c[3]]
print(d)
#判断2是否在列表里
if 2 in c:
    print("存在")
else:
    print("不存在")
#----------------------------
#b=[23,45,22,44,25,66,78]
#用列表解析完成下面练习题
#生成所有奇数组成的列表
n=[23,45,22,44,25,66,78]
k=[x for x in n if x%2 !=0]
print(k)
#输出结果["the content 23","the content 45"]
a=["the content"+ str(x) for x in n[0:2] ]
print(a)
#输出结果[25,47,24,46,27,68,80]
a=[2+x for x in n]
print(a)
#-------------------------------
#用range方法和列表推导的方法生成列表
#[11,22,33]
a=[x for x in range(11,44,11)]
print(a)
#------------------------------
#已知元祖a=(1,4,5,6,7)
#判断4是否在元祖里
a=(1,4,5,6,7)
if 4 in a :
    print("存在")
else:
    print("不存在")
b=[x for x in a if x==4 ]
print(b)
#元祖5修改成8
b=list(a)
b[2]=8
a=tuple(b)
print(a)
#-------------------------------
#setinfo=set("acbdfem") \ fininfo=("sabcdef")
#添加字符串对象"abc"到setinfo
setinfo=set("acbdfem")
setinfo.add("abc")
print(setinfo)
#删除setinfol里的成员m
setinfo.remove("m")
print(setinfo)
#求两个集合的交集和并集
fininfo=set("sabcdef")
a=(setinfo & fininfo)
b=(setinfo | fininfo)
print(a)
print(b)
#——--------------------------------
#字典的方法生成小学生管理系统
#属性：姓名，年龄 考试分数包括语文数学英文得分
liming={"姓名":"lingming","年龄":25,"语文":80,"数学":75,"英文":85}
xiaoqiang={"姓名":"xiaoqiang","年龄":15,"语文":60,"数学":95,"英文":83}
#敌营两个同学liming 年龄25，语文80，数学75，英文85、zhangqiang 年龄15，语文60，数学95，英文83
print(liming)
print(xiaoqiang)
#添加python课程的成绩 liming 60，zhangqiang 80
liming["python"]=60
xiaoqiang["python"]=80
print(liming)
print(xiaoqiang)
#zhangqiang 数学95 改为100
xiaoqiang["数学"]=100
print(xiaoqiang)
#删除liming的年龄
del liming["年龄"]
print(liming)
#zhangqiang同学的分数由高到底排序输出
a=[xiaoqiang["语文"],xiaoqiang["数学"],xiaoqiang["英文"],xiaoqiang["python"]]
a.sort()
print(a)
#删除城市属性，不存在返回beijing
print(xiaoqiang.pop("city","beijing"))
print(liming.pop("city","beijing"))
