# 列表 =》数组
a = ["a", "b", "c"]
"""
列表的常用操作
增加 insert(索引，数据)          在指定位置插入数据
     append(数据)               在末尾追加数据
     extend(列表2)              将列表2的数据追加到列表1
     
修改 列表[索引]=数据             修改指定的索引数据

删除 del 列表[索引]              删除指定索引的数据
     列表.remove[数据]           删除第一个出现的指定数据
     列表.pop                   删除末尾的数据
     列表.pop(索引)             删除指定索引的数据
     列表.clear                 清空列表
     
统计 len（列表）                 列表长度
     列表.count（数据）          数据在列表中出现的次数

排序  列表.sort()               升序
     列表.sort(reverse=true)    降序 
    列表.reverse()             逆序
"""
name_list=["zhangsan","lisi","wangwu"]
print(name_list[0])
print(name_list.index("lisi"))
name_list.insert(1,"zhangwuwu")
name_list.append("kk")
name2_list=["a","b"]
name_list.extend(name2_list)
name_list[0]="a"
del name_list[0]
name_list.remove("zhangwuwu")
name_list.pop()
name_list.pop(0)
name_list.clear()
name_list.append("feiyi")
name_list.insert(1,"yiran")
print(len(name_list))
name_list.sort()
name_list3=[2,1,5,6]
for name in name_list3:
    if name == 1:
        name=10
    print(name)
name_list3.sort()
print(name_list3)
name_list3.sort(reverse=True)
print(name_list3)
print(name_list)

