import socket

def main():
	udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	localAddr=("",8080)
	udp_socket.bind(localAddr)
	addr_ip=input("请输入你要发送的IP")
	addr_port=int(input("请输入你要放松的端口"))
	dest_msg=input("请输入想发送的内容")
	udp_socket.sendto(dest_msg.encode("utf-8"),(addr_ip,addr_port))
	udp_socket.recvfrom(1024)

	udp_socket.close()

if __name__ == '__main__':
	main()