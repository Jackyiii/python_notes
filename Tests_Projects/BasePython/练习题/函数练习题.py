#写一个函数代码，返回3个数的最大值
#a=123,b=345,c=444

#分别写两个函数，完成下面的功能
#提示一下用到的函数的**和*
#调用函数：ainfo(x=88,y=22,z=44)你定义的ainfo函数体里面的内容并且返回结果
#[22,44,88]
#调用函数cinfo=（x=88,y=22,z=44)你定义的cinfo函数体里面的内容并且返回结果
#("xaay","yaay","zaay")

def maxInt(data,n):
    if n==1:
        return data[0]
    else:
        max=data[0]
        for i in data[1:]:
            if max<i:
                max=i
        return max
a=123
b=555
c=444
data=[a,b,c]
print(maxInt(data,len(data)))

def ainfo(**kr):
    a=tuple(kr.values())
    a=sorted(a)
    return a
print(ainfo(x=88,y=22,z=44))

