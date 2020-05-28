import re

def main():
	#表示必须匹配1-2位
	res= re.match(r"速度与激情\d{1,2}","速度与激情12")
	print(res)
	res= re.match(r"速度与激情\d{5}","12345324题43453")
	print(res)
	#大括号表示必须匹配5位
	res= re.match(r"\d{5}","12345")
	print(res)
	#问号前面的表示可有可无
	res= re.match(r"010-?\d{6}","010123456")
	print(res)
	res= re.match(r"010-?\d{6}","010 123456")
	print(res)
	res= re.match(r"010-?\d{6}","010- 123456")
	print(res)
	#如果想要使用.匹配\n则传入第三个参数re.S
	html="ss sss \t ass ss "
	res= re.match(r".*",html,re.S).group()
	print(res)
	# *匹配前一个字符出现0次无限次
	# +匹配前一个字符出现至少一次
	# ?匹配前一个字符出现至多1次
	#{m}匹配前一个字符出现m次
	#{m,n}匹配前一个字符出现m-n次
if __name__ == '__main__':
	main() 