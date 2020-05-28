import time


def set_func(func):
	def call_func(num):
		start=time.time()
		print("authority_01")
		func(num)
		print("authority_02")
		end=time.time()
		print("is used %s"%(end-start))
	return call_func

@set_func
def test02(num):
	print("num is %s"%num)

test02(100)