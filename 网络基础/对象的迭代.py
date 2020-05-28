class Classmate(object):
	def __init__(self):
		self.name=list()
	
	def add(self,names):
		self.names.append(name)

	def __iter__(self):
		return ClassIterator(self)


class ClassIterator(object):
	def __init__(self,obj):
		self.obj=obj

	def __iter__(self):
		pass

	def __next__(self):
		return self.obj.name[0]


def main():
	c1=Classmate()
	c1.add("a")
	c1.add("b")
	c1.add("c")
	for c in c1:
		print(c)


if __name__ == '__main__':
	main()
