#isspace \r回车 \t制表 \n换行 unix \r windows \r\n
"""
isspace
isalnum
isalpha

数字
isdecimal
isdigit
isnumeric

istitle
islower
isupper

"""
str=" \t" #true
str1="sss" #false
str3="   \t\n\r" #true
print(str.isspace())
print(str1.isspace())
print(str3.isspace())

print("-"*10)

#判断是否只包含数字
#都不能判断小数
num_str="1"
num_str1="1.1"
num_str2="\u00b2"
num_str3="一千"
print(num_str.isdecimal())
print(num_str.isnumeric())
print(num_str.isdigit())
#小数测试
print(num_str1.isdecimal())
print(num_str1.isnumeric())
print(num_str1.isdigit())

#decimal数字
#digit 阿拉伯数字 unicode特殊数字
#numeric可以判断中文数字
print(num_str2)
print(num_str2.isdecimal())
print(num_str2.isnumeric())
print(num_str2.isdigit())
#能够判断中文的是numeric
print(num_str3)
print(num_str3.isdecimal())
print(num_str3.isnumeric())
print(num_str3.isdigit())
#开发经常使用decimal

print("#"*20)
#字符串查找和替换
"""
startswith(str)
endswith(str)
find(str,start=0,end=len(str))
replace()
"""
hello="hello world"
print(hello.startswith("hello",0,len(hello)))
print(hello.startswith("hello",1,len(hello)))
print(hello.endswith("ld",0,len(hello)))
print(hello.endswith("world",0,len(hello)))
print(hello.find("l"),2,len(hello))
#index报错，find会返回-1
hello="hello hello,hello world"
#replace会返回新的字符串需要变量接收
hello=hello.replace("hello","yi",2)
print(hello)

print("*"*20)
#文本对齐
poem=[
    "等落",
    "王焕枝",
    "黄河入海流",
    "千里目"
]
for p in poem:
    print("|%s|"%p.ljust(10,"。"))
    #print("|%s|" % p.center(10, "。"))
print("$"*20)
#去除空白字符
strp=" s "
print(strp)
strp=strp.strip()
print(strp)
