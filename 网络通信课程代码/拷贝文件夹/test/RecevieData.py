import socket


def  main():

	udpSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	#设置自身的IP和端口
	addr=("",7788)
	#数据绑定
	udpSocket.bind(addr)

	while True:
		#接收数据
		recvData=udpSocket.recvfrom(1024)
		contentData=recvData[0]
		infoData=recvData[1]
		print("ip:%s,port:%s,内容是:%s"%(str(infoData[0]),str(infoData[1]),contentData.decode("utf-8")))
		#关闭并且释放内存
	udpSocket.close()		

if __name__ == '__main__':
	main()
