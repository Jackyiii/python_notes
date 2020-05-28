def set_func(func):
	def call_func():
		print("authority_01")
		print("authority_02")
		func()
	return call_func
@set_func
def test01():
	print("test01")

# re=set_func(test01)
# re()
test01()