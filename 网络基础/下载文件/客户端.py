import socket


def main():
	#创建套接字
	socket_client_tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#连接端口
	dest_ip=input("请输入连接的服务器")
	dest_port=int(input("请输入端口"))
	dest_info=(dest_ip,dest_port)
	socket_client_tcp.connect(dest_info)
	#获取下载文件的名字
	file_name=input("请输入下载文件的名字:")
	#发送数据到服务器
	socket_client_tcp.send(file_name.encode("utf-8"))
	recv_data=socket_client_tcp.recv(1024)#接收数据
	#将数据保存到文件中
	#if recv_data:
	with open("[new]"+file_name,"wb") as f:
		f.write(recv_data)
		print("写入成功")
	print("关闭成功")
	socket_client_tcp.close()
 






if __name__ == '__main__':
	main()