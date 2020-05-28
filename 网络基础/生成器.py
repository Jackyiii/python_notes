def create_number(allnum):
	a=0
	b=1
	a,b=0,1
	current_num=0
	while current_num<allnum:
		yield a 
		a,b=b,a+b
		current_num+=1

def main():
	obj=create_number(10)
	ret=next(obj)
	print(ret)
	ret=next(obj)
	print(ret)


if __name__ == '__main__':
	main()