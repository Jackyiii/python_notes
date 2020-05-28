import re

def main():
	res=re.match(r"速度与激情","速度与激情2")
	print(res)
	res=re.match(r"速度与激情\d","速度与激情2")
	print(res)
	res=re.match(r"速度与激情","速度与激情2")
	print(res.group())
	res=re.match(r"速度与激情[12]","速度与激情2")
	print(res)
	res=re.match(r"速度与激情[1-36-8]","速度与激情4")
	print(res)
	res=re.match(r"速度与激情[1-36-8]","速度与激情78")
	print(res)
	res=re.match(r"速度与激情\s\d","速度与激情\t1")
	print(res)
	res=re.match(r"速度与激情.","速度与激情1").group()
	print(res)
	res=re.match(r"速度与激情.","速度与激情a").group()
	print(res)
	#.匹配任意1个字符除了\n
	#[]匹配[]中列举的字符
	#\d匹配数字0-9
	#\D匹配非数字
	#\s匹配空白 空格和tab
	#\S匹配非空白
	#\w匹配单词字符a-z，A-Z 0-9 _
	#\W匹配非单词字符
if __name__ == '__main__':
	main()