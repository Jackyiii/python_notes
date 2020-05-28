import multiprocessing


def download_from_web(q):
	"模拟下载数据"
	data = [12,14,1,5,7]
	for temp in data:
		q.put(temp)
	print("已存入数据")

	
def analysis_data(q):
	"数据处理"
	waiting_data=list()
	while True:
		data=q.get()
		waiting_data.append(data)
		if q.empty():
			print("队列已空")
			break
	print("数据拷贝完毕%s"%waiting_data)

def main():
	q=multiprocessing.Queue()
	p1=multiprocessing.Process(target=download_from_web,args=(q,))
	p2=multiprocessing.Process(target=analysis_data,args=(q,))
	p1.start()
	p2.start()


if __name__ == '__main__':
	multiprocessing.freeze_support()
	main()