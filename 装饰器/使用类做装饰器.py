class Test(object):
	def __init(self,func):
		self.func=func

	def __call__(self):
		print("装饰器添加的功能呢")
		self.func()
		return self.func()



#相当 get_str=Test(get_str)
#@Test.static
@Test
def get_str():
	return "hahah"

print(get_str())