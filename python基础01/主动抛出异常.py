def pwdInput():
    pwd = input("请输入密码")
    if len(pwd) >= 8:
        return pwd

    ex = Exception("密码长度不够")
    raise ex


try:
    print(pwdInput())
except Exception as result:
    print("异常是%s"%result)
