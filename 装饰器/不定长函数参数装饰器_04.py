def set_func(func):
	print("___开始装饰器")
	def call_func(*args,**kwargs):
		print("这是验证权限")
		print("这是验证权限2")
		#通用装饰器
		return func(*args,**kwargs)
	return call_func

@set_func
def test(num,*args,**kwargs):
	print("test_01:%d"%num)
	print("test_02",args)
	print("test_03",kwargs)
	return "ok","yes"

ret=test(100)
test(100,200)
test(100,200,300,mm=100)
print(ret)