import select
import socket
import re

def service_client(new_socket,request):
	request_lines=request.splitlines()
	file_name=""
	ret=re.match(r"[^/]+(/[^ ]*)",request_lines[0])
	if ret:
		file_name=ret.group(1)
		if file_name=="/":
			file_name="/index.html"

	try:
		f=open("./html"+file_name,"rb")
	except:
		response="HTTP/1.1 404 NOT FOUND\r\n"
		response+="\r\n"
		response+="file not found"
		new_socket.send(response.encode("utf-8"))
	else:
		html_content=f.read()
		f.close()
		response_body=html_content
		response_header="HTTP/1.1 200 OK\r\n"
		response_header+="Content-Length: %d\r\n"%len(response_body)
		response_header+="\r\n"
		response =response_header.encode("utf-8")+response_body
		new_socket.send(response)

def main():
	#创建套接字
	tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#绑定
	tcp_server_socket.bind(("",7890))
	#监听
	tcp_server_socket.listen(128)
	#套接字变为非堵塞
	tcp_server_socket.setblocking(False)
	#创建epoll对象
	epl=select.epoll()
	#将监听套接字的fd注册到epoll中
	epl.register(tcp_server_socket.fileno(),select.EPOLLIN)
	fd_event_dict=dict()
	
	while True:
		#默认堵塞知道os检测到数据到来，通过事件方式通知告诉这个程序，此时会解堵塞
		fd_event_list=epl.poll()
		#[(fd,event),(套接字对应的文件描述符，这个文件描述符到底是什么事件 例如recv)]
		for fd,event in fd_event_list:
			if fd==tcp_server_socket.fileno():
				new_socket,client_addr=tcp_server_socket.accept()
				epl.register(new_socket.fileno,select.EPOLLIN)
				fd_event_dict[new_socket.fileno()]=new_socket
			elif event==select.EPOLLIN:
				#判断已经连接的客户端是否有发送数据过来
				recv_data=fd_event_dict[fd].recv(1024).decode("utf-8")
				if recv_data:
					service_client(fd_event_dict[fd],recv_data)
				else:
					fd_event_dict[fd].close()
					epl.unregister(fd)
					del fd_event_dict[fd]
	tcp_server_socket.close()






if __name__ == '__main__':
	main()