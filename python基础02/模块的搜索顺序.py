"""
搜索当前的目录指定模块名的文件，如果有就直接导入
如果没有就搜索系统目录
开发时注意不要和系统的模块文件重名

"""
import random
rand=random.randint(0,10)#生成0-10随机数
print(rand)
print(random.__file__)