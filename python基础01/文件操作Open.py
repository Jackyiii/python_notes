"""
传入要打开的文件名，返回对象
read一次性的读入并且返回
close负责关闭文件

"""
#打开文件
file=open("readMe.txt")
text=file.read()
print(text)
print(len(text))
print("-"*10)

text=file.read()
print(text)
print(len(text))

file.close()
#文件指针--从哪个位置读取数据
#文件读取完后指针会指向末尾