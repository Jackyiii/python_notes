#字典是无序的 他不能通过偏移进行存取，只能通过键值对来存取
#字典={'key':value}key类似我们实现的钥匙，而value是锁，一个钥匙对应一个锁
#特点内部没有顺序，通过键来读取内容，可以嵌套。方博啊吗我怕，方便我们组织多种的数据结构，并且可以修改里面的内容
#属于可变的类型
#组成字典的键必须是不可变的数据类型，比如数字，字符串，元祖等，列表等可变的对象不能作为键
#1创建字典{} dict()_
#info={'name':'lilei',"age":23}
#添加内容a['xx']="xx"
#update参数是一个字典类型，他会覆盖相同键的值
a={'a':1,'b':2,'c':4}
b={'a':'c',1:2,'c':4}
print(b)
c={'a':[1,2,3]}
c['a'][2]=4
print(c)
#键是不可变的数据类型
#数字，字符串，元祖可以作为字典的键，列表不可以
#字典是无序的
#两种方法创建字典
a={'a':1,'b':2} #1
a=dict(name='li',hi='si')
print(a)
#字典的添加操作
a["iphone"]="iphoneZ"
print(a)
#字典的修改操作
a["iphone"]="htc"
print(a)
a.update({"iphone":"samsung","city":"pekin"})
print(a)
#字典的删除操作
del a["city"]
print(a)
#字典的清空
b={"xiaoming":"shuai","limei":"cool"}
b.clear()
print(b)
#字典的pop方法，会讲字典中的key返回出来并且将字典的对应的key和值删除
c={"yi":1,"fei":2}
d=c.pop("yi")
print(d)
print(c)
#字典传入的pop是key，而list传入的是索引下标
#对比字典和list的pop方法的区别是，list的pop方法如果输入不存在下标，会抛出异常，然而字典第二个参数可以返回自定义的参数
#list 的in 判断元素是否在列表中如果在返回ture不在返回false
#has_key()
a=[1,2,3,4]
b=(5 in a)
print(b)
a={"yi":"cool","fei":"so cool"}
#print(a.has_key("cool"))
if "yi" in a.keys():
    print("cooooook")
#keys()打印所有key values()打印所有的value值
if"cool" in a.values():
    print("yes")
#get方法
b=a.get("yi")
print(b)
#如果get方法返回一个不存在的，会打印空，但是是NoneType方法,但是第二个参数可以选择设定好的默认值
b=a.get("daye","heheh")
print(b)



