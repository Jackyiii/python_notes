#import 模块名 as 模块别名
#模块别名.
#from 模块 import 模块工具
#可以使用as起一个别名
from  模块测试1 import Dog as cat
d=cat("史努比")
d.play()
#如果两个模块导入相同的函数名，则第二个会覆盖掉第一个
#如果从模块中导入全部的工具会导入全部的工具
from 模块测试1 import *
a=demo1()
print(a)
#但是不推荐使用
