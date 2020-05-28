import re
name_list=["name1","_name","1name","__name__"]
for name in name_list:
	#$必须规范到结尾
	#^以判断谁开始
	ret=re.match(r"^[a-zA-Z_]+[\d_a-zA-Z]*$",name)
	if(ret):
		print("变量名%s符合"%ret.group())
	else:
		print("变量名%s非法"%name)