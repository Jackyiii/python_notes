import socket

def main():
	#1.创建套接字
	tcp_socket_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#2.连接服务器
	#tcp_socket_client.connect("192.168.0.1",8080)
	server_ip=input("ip")
	server_port=int(input("port"))
	server_addr=(server_ip,server_port)
	tcp_socket_client.connect(server_addr)
	#3.发送数据
	send_data=input("data")
	tcp_socket_client.send(send_data.encode("utf-8"))
	#4.关闭套接字
	tcp_socket_client.close()

if __name__ == '__main__':
	main()
