import time
import threading

g_nums=1000000
mutex=threading.Lock()

def test1(num):
	global g_nums
	for i in range(num):
		mutex.acquire()
		g_nums+=1
		mutex.release()
	print("test1=%s"%g_nums)


def test2(num):
	global g_nums
	for j in range(num):
		mutex.acquire()
		g_nums+=1
		mutex.release()
	print("test2=%s"%g_nums)


def main():
	t1=threading.Thread(target=test1,args=(1000000,))
	t2=threading.Thread(target=test2,args=(1000000,))
	t1.start()
	t2.start()
	time.sleep(2)
	print("main=%s"%g_nums)

if __name__ == '__main__':
	main()