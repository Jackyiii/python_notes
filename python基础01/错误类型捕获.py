try:
    num = int(input("请输入一个整数"))
    aresult = 8 / num
    print(aresult)
# except ZeroDivisionError:
#     print("分母不能为0")
except ValueError:
    print("请输入整数")
# 捕获未知错误
except Exception as result:
    # print("捕获未知错误")
    print("未知异常%s" % result)
