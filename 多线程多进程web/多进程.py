import multiprocessing
import socket
import re

def service_client(new_socket):
	"""为用户返回数据"""
	request=new_socket.recv(1024).decode("utf-8")
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
	else:
		html_content=f.read()
		f.close()
		response="HTTP/1.1 200 OK\r\n"
		response+="\r\n"
		new_client.send(response.encode("utf-8"))
		new_client.send(html_content)  

def main():
	#创建套接字
	tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#绑定套接字
	tcp_server_socket.bind(("",7890))
	#套接字变为监听模式
	tcp_server_socket.listen(128)
	#等待用户输入
	while True:
		new_socket,socket_addr=tcp_server_socket.accept()

	#为用户服务
		p=multiprocessing.Process(target=service_client,args=(new_socket,))
		p.start()
		new_socket.close()
	#关闭
	tcp_server_socket.close()

if __name__ == '__main__':
	main()