def set_level(level_num):
	print("开始权限验证")
	def set_func(func):
		def call_func(*args,**kwargs):
			if level_num==0:
				print("__权限验证0")
			elif level_num==1:
				print("__权限验证1")
			return func()
		return call_func
	return set_func

@set_level(0)
def test():
	print("test-1")
	return "ok_1"

@set_level(1)
def test02():
	print("test-2")
	return"ok_2"

test()
test02()

# 开始权限验证
# 开始权限验证
# __权限验证0
# test-1
# __权限验证1
# test-2