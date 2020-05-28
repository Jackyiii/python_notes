xiaoming = {"name": "xiaoming",
            "age": 2,
            "profession": "teacher"
            }
print(xiaoming["name"])
print(xiaoming)
# 增加和修改
xiaoming["name"] = "yi"
print(xiaoming["name"])
xiaoming["yiran"] = "yuan"
print(xiaoming)
xiaoming.pop("age")
print(xiaoming)

# 统计键值对的数量
print(len(xiaoming))
# 合并字典
xiaoqiang = {"name": "xiaoqiang", "height": 1.4}
xiaoming.update(xiaoqiang)
print(xiaoming)
for k in xiaoming:
    print("Key=%s : Value=%s" % (k, xiaoming[k]))
# 列表与字典的应用场景
# 字典保存一个数据的复杂信息
# 放在同一个列表变量中
card_list = [
    {"name": "xiaoqiang",
     "age": 30
     },
    {"name": "feifei",
     "age": 29
     }
]
for cardinfo in card_list:
    # print(cardinfo)
    for dicinfo in cardinfo:
        if dicinfo == "name":
            print(cardinfo[dicinfo])
