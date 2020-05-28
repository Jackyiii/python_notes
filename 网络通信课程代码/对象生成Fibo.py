class Fibonacci(object):
	def __init__(self,allnum):
		self.current_number=0
		self.a=0
		self.b=1
		self.allnum=allnum

	def __iter__(self):
		return self

	def __next__(self):
		if self.current_number<self.allnum:		
			res=self.a

			self.a,self.b=self.b,self.a+self.b
			self.current_number+=1
			return res 
		else:
			raise StopIteration

def main():
	fi=Fibonacci(10)
	for f in fi:
		print(f)

if __name__ == '__main__':
	main()