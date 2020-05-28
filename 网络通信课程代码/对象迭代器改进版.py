import time


class Classmate(object):
	def __init__(self):
		self.names=list()
		self.curr_num=0
	def __iter__(self):
		return self 
	
	def add(self,name):
		self.names.append(name)

	def __next__(self):
		if self.curr_num<len(self.names):
			res=self.names[self.curr_num]
			self.curr_num+=1
			return res
		else:
			raise StopIteration


def main():
	c1=Classmate()
	c1.add("a")
	c1.add("b")
	c1.add("c")
	c1.add("d")
	for n in c1:
		print(n)
		time.sleep(1)

if __name__ == '__main__':
	main()