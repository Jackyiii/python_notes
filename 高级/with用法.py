from contextlib import contextmanager

class File(object):
	def __init__(self,filename,mode):
		self.filename=filename
		self.mode=mode

	def __enter__(self):
		print("entering")
		self.f=open(self.filename,self.mode)
		return self.f

	def __exit__(self,*args):
		print("will exit")
		self.f.close()


with File("out.txt","w") as f:
	print("writing")
	f.write("hellp")

@contextmanager
def  my_open(path, mode):
	#相当于enter
	f=open(path,mode)
	#相当于之后的
	
	yield f
	f.close()

with my_open("out.txt","w") as f:
	f.write("hellor")