"""
用户选择不同的功能
根据功能执行不同的任务
用户名片需要记录用户的姓名电话QQ和邮件
用户可以查询到指定的名片并进行修改或者删除名片
"""

a0 = "欢迎使用[名片管理系统]V1.0"
a1 = "新建名片"
a2 = "显示全部"
a3 = "查询名片"
a4 = "退出系统"
strName = "姓名"
strTel = "电话"
strQQ = "QQ"
strEmail = "Email"
name = ""
tel = 0
QQ = ""
email = ""
#TODO 用法，代做的任务
card = [
    # {"name": name, "tel": tel, "QQ": QQ, "email": email},
    # {"name": name, "tel": tel, "QQ": QQ, "email": email},
    # {"name": name, "tel": tel, "QQ": QQ, "email": email}
]


# --------------------------------------------------
# 判断用户输入,显示用户输入
def caseInput(key):
    if key == 1:
        print("你输入的是%s,正在%s..." % (key, a1))
        createCard(name, tel, QQ, email)
        main()
    elif key == 2:
        print("你输入的是%s,正在%s..." % (key, a2))
        LookAtALl()
        main()
    elif key == 3:
        print("你输入的是%s,正在%s..." % (key, a3))
        InsertDel()

    elif key == 0:
        print("你输入的是%s,正在%s..." % (key, a4))
    else:
        print("对不起你输入的有误请重新输入")


# --------------------------------------------------
# 创建名片
def createCard(name, tel, QQ, email):
    card_dict = {}
    i = 0
    print("请输入名片%s并以回车结束" % (strName))
    name = input()
    print("%s是:%s" % (strName, name))
    card_dict["name"] = name
    print("")

    print("请输入名片%s并以回车结束" % (strTel))
    tel = int(input())
    print("%s是:%d" % (strTel, tel))
    card_dict["tel"] = tel
    print("")

    print("请输入名片%s并以回车结束" % (strQQ))
    QQ = input()
    print("%s是:%s" % (strQQ, QQ))
    card_dict["QQ"] = QQ
    print("")

    print("请输入名片%s并以回车结束" % (strEmail))
    email = input()
    print("%s是:%s" % (strEmail, email))
    card_dict["email"] = email
    print("")

    print("请确认名片的信息，姓名是:%s, 电话是:%s, QQ是%s, Email:%s" % (name, tel, QQ, email))
    print("确认添加请选1，取消请选0")

    confirm = int(input())
    if confirm == 1:
        print("创建成功")
        card.append(card_dict)
    elif confirm == 0:
        print("创建已取消")


# --------------------------------------------------
# 显示全部名片
def LookAtALl():
    print("展示全部名片信息")
    print(card)


# --------------------------------------------------
# 修改信息和删除
def InsertDel():
    insertDel = 0
    modifier = ""
    print("修改请选1，删除选2")
    insertDel = int(input())
    if insertDel == 1:
        print("请输入你想要修改信息的姓名")
        modifier = input()
        for dicList in card:
                #print(dicList[key])
                if dicList["name"] == modifier:
                    print("已找到名片%s"%(dicList["name"]))
                    #print("shhshshs"+dicList)
                    break
        else:
            print("没有找到")
    elif insertDel == 2:
        print("删除")


# --------------------------------------------------
# 展示面板
def main():
    print("*" * 50)
    print("%s\n\n1.%s\n2.%s\n3.%s\n\n0/%s" % (a0, a1, a2, a3, a4))
    print("")
    print("*" * 50)
    # 接收用户输入
    key = int(input())
    caseInput(key)


# --------------------------------------------------
# 主函数
main()

# --------------------------------------------------
