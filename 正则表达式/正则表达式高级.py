#search
#ret=re.search(r"\d+","阅读次数为999")
#ret.group()
#findall返回列表不需要group返回所有数据
#ret=re.findall(r"\d+")
#sub 替换
#re.sub(r"\d+",'998',"python=997,c++=1024")
#sub支持函数调用ret=re.sub(r"\d+",add,"python=997")
#def add(temp):strNum=temp.group() num=int(strNum)+1 return str(num)
#split 根据匹配进行切割字符串，并返回列表
#ret=re.split(r":| ","info:xiaoZhang 33 shandong)
#结果["info","xiaoZhang","33","shandong"]