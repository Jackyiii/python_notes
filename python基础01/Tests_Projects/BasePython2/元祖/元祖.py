#元祖定义完成不能修改
#特定应用场景，保存不同的数据类型
#列表也可以但是，经常使用相同的数据类型
info_tuple=("fy")
print(type(info_tuple))
#如果内部数据只有一个或变成引号里面的类型
#如果只包含一个元素的元祖
info_tuple2=("fy",)
print(type(info_tuple2))
info_tuple3=()
print(type(info_tuple3))

info_tuple4=("zhangsan",2,15,2)
print(info_tuple4[1])
print(info_tuple4.index(2))
print(info_tuple4.count(2))
print(len(info_tuple4))
#for可以遍历非数字型的变量
for k in info_tuple4:
    print(k)

#因为元祖中保存的数据类型通常不一样，所以很少遍历

#元祖的应用场景
#函数的参数和返回值，函数可以接收任意多个参数，可以一次性返回多个返回值
#格式字符串（"%d%s"%（元祖））
#列表不可以被修改保护数据
info_tuple5=("xiaoming",5,1.85)
print("姓名%s，年龄%d，身高%.2f"%info_tuple5)
info_tuple6=(1,3,2,3,5,7,4)
print(info_tuple6)
info_list6=[1,4,2,3,4,52,1,2]
print(info_list6)