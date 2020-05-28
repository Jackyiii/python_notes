import time
import socket


tcp_server_tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_server_tcp.bind(("",7890))
tcp_server_tcp.listen(128)
tcp_server_tcp.setblocking(False)#设置套接字为非阻塞
client_socket_list=list()

while True:
	time.sleep(0.5)
	try:
		new_socket,new_addr=tcp_server_tcp.accept()
	except Exception as ret:
			print("——没有新客户到来")
	else:
		print("只要没有异常，就来了一个新客户")
	for client_socket in client_socket_list:
		try:
			recv_data=client_socket.recv(1024)
		except Exception as ret:
			print("--这个客户端没有发送数据")
		else:
			if recv_data:
				print("有数据")
			else:
				client_socket_list.remove(client_socket)
				client_socket.close()