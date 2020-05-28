# age = float(input("请输入年龄"))
# if age >= 18:
#     print("你可以进入网吧")
# else:
#     print("你的年龄为%d,您小于18不能进入" % age)
"""
逻辑运算符
or
and
not
"""

# holidayName=input("请输入节日")
# if holidayName=="情人节":
#     print("购买玫瑰")
# elif holidayName=="平安夜":
#     print("买糖")
# elif holidayName=="生日":
#     print("买包")
# else:
#     print("你完蛋了")
#
hasTicket = True
KnifLen = 19
if KnifLen <= 18:
    print("可以进入安检")
    if hasTicket:
        print("可以通过")
        # hahha
        # heihei
    else:
        print("不允许上车")
else:
    print("长度为%.1f不允许上车" % KnifLen)
#tab进行缩进， shift减少缩进
