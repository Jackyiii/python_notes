import re
#coding=utf-8
#导入re模块
#import re
#使用match方法进行匹配操作
#result=re.match(正则表达式,要匹配的字符串)->python
#如果上一步匹配到数据，咋可以使用group方法来踢去数据
#result.group()

# result=re.match("itcast","itcast.cn")
# a=result.group()
# print(a)
# print(result)

res= re.match(r"[hH]ello","Hello world")
print(res)