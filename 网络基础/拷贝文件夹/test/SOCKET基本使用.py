import socket
def main():
	udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	#可以是套接字
	udp_socket.sendto(b"开心",("172.20.10.8",8080))#对方的ip和端口
	#离开
	print("run")
if __name__== "__main__":
	main()
