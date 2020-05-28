def set_func1(func):
	def call_func():
		return "<h1>"+func()+"</h1>"
	return call_func

def set_func2(func):
	def call_func():
		return "<div>"+func()+"</div>"
	return call_func

@set_func2
@set_func1
def test01():
	return "hello"

print(test01())