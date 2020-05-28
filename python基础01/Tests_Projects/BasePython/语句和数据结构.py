import string
a="dadoahAWAJPDWo83054dacvnghewoeacdf"
print(sorted(a,reverse=True))
#数字，大写字母小写字母从小到大顺序排起
a=[x for x in a if not x.isdigit()]
a="".join(a)
print(a)
a="yifei"
print("".join(sorted(a,key=str.upper)))
a="li lei"
s=a.replace("lei","yi")
print(s)
s="yifei"
c=str.maketrans("i","I")
print(s.translate(c))
d=str.maketrans("123","abc")
f="1233a"
print(f.translate(d))

#translate 第二个参数是删除
# g=str.maketrans("124","abc")
# f="1234532"
# print(f.translate(g,"1"))
g=open("a.txt","w")
g.write("hello wolrd\n hahah")
g.close()

with open("a.txt","a") as g:
    g.write("hello again")




