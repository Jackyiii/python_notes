import threading
import time

class Mythread(threading.Thread):
	def run(self):
		self.name="nihao"
		
		for i in range(3):
			time.sleep(1)
			msg="I'm"+self.name+"@"+str(i)
			print(msg)
			self.login()
	def login(self):
		print(self.name+"login")


def main():
	t=Mythread()
	t.start()
if __name__ == '__main__':
	main()