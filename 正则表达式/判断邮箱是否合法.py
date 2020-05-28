import re

#以下划线英文字母或者数字开头4-20位

def main():
	while True:
		#提问请输入邮箱
		correct_email=""
		email=input("请输入一个邮箱")
		correct_email=verifier_mail(email)


def verifier_mail(email):
	res=re.match(r"^[a-zA-Z_][a-zA-Z\d_]{4,20}@(163|126|gmail)\.com$",email)
	if(res):
		print("%s邮箱成功，并且是%s邮箱"%(res.group(),res.group(1))
		return res.group()

	else:
		print("请输入正确的邮箱,%s格式有误"%email)	

#\num 引用分组num匹配到的字符串
#(?P<name>) 分组别名
#（？P=name）引用别名为name分组匹配到的字符串
#re.match(r"^<(?P<p1>\w*)><(?P<p2>\w*)>.*</(?P=p2)></(?P=p1)>")
#判断用户输入的邮箱是否合法
if __name__ == '__main__':
	main()