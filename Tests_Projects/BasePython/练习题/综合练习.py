import os
#1已知字符串a="aAsmr3idd4bgs7Dlsf9eAF"
a="aAsmr3idd4bgs7Dlsf9eAF"
#1.1将字符串中大写改为小写小写改为大写
a1=[]
a2=""
for x in a:
    if(x.islower()):
        a1.append(x.upper())
    elif(x.isupper()):
        a1.append(x.lower())
a1="".join(a1)
print(a1)
#1.2将a的数字取出组成新的字符串
num=[]
for current_num in a:
    if(current_num.isnumeric()):
        num.append(current_num)
num="".join(num)
print(num)
print("".join([s for s in a if s.isdigit()]))
#1.3统计字符串a中每个字母出现的次数忽律大小写并输出一个字典{"a":4,b:"2"}
a=a.lower()
print(dict([(x,a.count(x)) for x in set(a)]))

#1.4去除字符串多次出现的字母，仅仅保留最先出现的一个"abcabb" abc
a_list= list(a)
set_list=list(set(a_list))
set_list.sort(key=a_list.index)
print("".join(set_list))
#1.5将字符串进行反转
a="aAsmr3idd4bgs7Dlsf9eAF"
b=list(a)
b.sort(reverse=True)
print([x for x in b if x is not int])
#print("---".join(x))
print(a[::-1])
#1.6去除a字符串额数字后将字母进行重新排序大写A在小写a前面
a_lower_list=[]
a_supper_list=[]
l=sorted(a)
for x in l:
    if x.islower():
        a_lower_list.append(x)
    elif x.isupper():
        a_supper_list.append(x)
    else:
        pass
for y in a_supper_list:
    y_lower=y.lower()
    if y_lower in a_lower_list:
        a_lower_list.insert(a_lower_list.index(y_lower),y)
print("".join(a_lower_list))
#1。7判断"boy"是否每个字符都在a里面如果是为true 否则为false

#1。8假如新的girl bired dirty
#1。9求字符串出现频率最高的字母
a="aAsmr3idd4bgs7Dlsf9eAF"
l=([(x,a.count(x)) for x in set(a)])
l.sort(key=lambda k:k[l],reverse=True)
print(l[0][0])
#2命令行import this统计该文档be is than出现的次数
#3字节为102324123499123计算kb和mb分别的大小
#4已知a=[1,2,3,6,8,9,10,14,17]·转化为字符串输出
