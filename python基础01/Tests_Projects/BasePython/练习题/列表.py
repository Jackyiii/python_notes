#已知元祖a=(1,2,3)利用list方法输出下面结果
a=(1,2,3)
b=list(a)
b[2]=4
print(b)
#输出列表[1 love python,2 love python,...10 love python]
#输出[(0,0).(0,2),(2,0)(2,2)]
#a=[1,2,3] / b=a[:] / dela
y=[str(x)+" love python" for x in range(1,11)]
print(y)
a=[1,2,3]
print(id(a))
b=a[:]
a.clear()
#del a
print(b)
print(a)
print(id(a))
print(id(b))
#因为b的引用指向了[1,2,3]的内存地址，
