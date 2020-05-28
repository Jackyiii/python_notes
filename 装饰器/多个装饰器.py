def add_qx(func):
	
	def call_func(*args,**kwargs):
		print("__验证1")
		return func(*args,**kwargs)
	print("__开始装1的功能")
	return call_func

def add_xx(func):
	print("__开始装2的功能")
	def call_func(*args,**kwargs):
		print("__验证2")
		return func(*args,**kwargs)
	return call_func

@add_qx
@add_xx
def test1():
	print("1")

test1()
