import socket
def service_client(new_socket):
	request=new_socket.recv(1024)
	print(request)
	response="HTTP/1.1 200 OK\r\n"
	response+="\r\n"
	response+="hello world"
	new_socket.send(response.encode("utf-8"))
	new_socket.close()


def main():
	#创建套接字
	tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#绑定套接字
	addr=""
	port=7890
	addr_port=(addr,port)
	tcp_server_socket.bind(addr_port)
	#套接字设为被动监听
	tcp_server_socket.listen(128)
	#等待用户连接
	while True:
		new_socket,client_addr=tcp_server_socket.accept()
		#用户服务
		service_client(new_socket)
		#关闭套接字
	tcp_server_socket.close()



if __name__ == '__main__':
	main()