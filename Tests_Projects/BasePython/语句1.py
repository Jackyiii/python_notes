#print方法
#print("1","4","5","7")
#用print输出到文件>>重定向符号
#f=open("print.txt","w")
#print >> f, "Hello world"
#print >> f,"Hello world again"
#print >> f,"hello world","Hhahahha"
#f.close()

#控制流语句
if True: #条件
    print("yes")#执行代码块

a=4
if a==4:
    print("is true")
# and or not相当于非   is是否引用了同一个数据对象 "1313" is True 字符串 和bool的数据对象因此不同
#==左右两边值是否相同
if True or False:
    print("dui")
else:
    print("cuo")

if False is True:
    print("is 是数据对象相同")

if 1==True:
    print("true=1")

if not False:
    print("非")

if True:
    print("True")
elif not True:
    print("not true")
else:
    pass
##三元表达式
4 if True else 3
if(True):
    print(4)
else:
    print(3)