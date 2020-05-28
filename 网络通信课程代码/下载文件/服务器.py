import socket


def send_2_file(new_client,client_addr):
	#1.接收客户端需要下载的文件名
	#接收发送过来的数据需要下载的文件名
	file_name=new_client.recv(1024).decode("utf-8")
	print("客户端(%s)需要下载的文件是%s"%(str(client_addr),file_name))
	file_content=None
	try:
		f=open(file_name,"rb")
		file_content=f.read()
		f.close()
	except Exception as e:
		print("没有要下载的文件(%s)"%file_name)
	#发送数据给客户端
	if file_content:
		print("发送成功")
		print(file_content)
		new_client.send(file_content)	


def main():
	#创建套接字
	socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#绑定端口
	ip_port=("",7892)
	socket_server.bind(ip_port)
	#变为监听模式
	socket_server.listen(128)
	while True:
		new_client,client_addr=socket_server.accept()
		# 调用发送数据的函数
		send_2_file(new_client,client_addr)
		#关闭新客户
		new_client.close()
	#关闭整个套接字
	socket_server.close()


if __name__ == '__main__':
	main()