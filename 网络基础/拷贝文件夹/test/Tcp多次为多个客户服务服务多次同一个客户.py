import socket
def main():
	#创建套接字
	tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#绑定本地信息 
	addr_info=("",7892)
	tcp_server_socket.bind(addr_info)
	#设置为监听模式
	tcp_server_socket.listen(128)
	#循环为多个客户端服务
	while True:
		print("等待一个客服端连接")
		new_client_socket,client_addr=tcp_server_socket.accept()
		client_addr_str=str(client_addr)
		print("%s新的客户端到来:"%client_addr_str)

		#循环为这个客户端服务多次
		while True:
			recv_data=new_client_socket.recv(1024)
			print("%s:%s"%(client_addr_str,recv_data.decode("utf-8")))
			#如果recv堵塞有两种方式，1客户端发送数据过来，2客户端调用close关闭recv解堵塞
			if recv_data:
				new_client_socket.send("service for you".encode("utf-8"))
			else:
				break
		#关闭accept返回的套接字，意味着不会为这个客户端服务
		new_client_socket.close()
	tcp_server_socket.close()
if __name__ == '__main__':
	main()