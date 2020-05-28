import socket
def main():
	udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	#可以是套接字
	#发送任意数据
	while True:
		send_data=input("send your message")
		if send_data=="exit":
			break
		udp_socket.sendto(send_data.encode("utf-8"),("172.20.10.8",8080))#对方的ip和端口
	#离开
	print("run")
if __name__== "__main__":
	main()
