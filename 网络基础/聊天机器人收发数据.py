import socket


def sendtoMsg(udp_socket):
	dest_ip=input("请输入发送的ip")
	dest_port=int(input("请输入发送的端口"))
	dest_msg=input("请输入发送的消息")
	dest_info=(dest_ip,int(dest_port))
	udp_socket.sendto(dest_msg.encode("utf-8"),dest_info)
	print("发送成功")

def recvMsg(udp_socket):
	print("正在接收数据...")
	recv_data=udp_socket.recvfrom(1024)
	print("%s向你发送了:%s"%(str(recv_data[1]),recv_data[0].decode("utf-8")))

def main():
	udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	local_addr=("",7879)
	udp_socket.bind(local_addr)

	while True:

		#欢迎界面
		print("欢迎来到聊天机器人程序")
		print("-"*20)
		print("发送数据请选 -- 1")
		print("接收数据请选 -- 2")
		print("退出请选择 -- 0")
		print("-"*20)
		use_op=input()
		if use_op=="1":
			#发送数据
			sendtoMsg(udp_socket)
		elif use_op=="2":
			#接收数据
			recvMsg(udp_socket)
		elif use_op=="0":
			#退出程序
			break
		else:
			print("error!")
	udp_socket.close()

if __name__ == '__main__':
	main()