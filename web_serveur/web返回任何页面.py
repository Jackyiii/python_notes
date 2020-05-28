import socket
import re
import os
def service_client(new_client):
	#接收发送的请求
	request=new_client.recv(1024).decode("utf-8")
	request_lines=request.splitlines()
	print("")
	print(">"*20)
	print(request_lines)
	file_name=""
	path=os.path.expanduser("~/Desktop/Python/web_serveur/html")
	ret=re.match(r"[^/]+(/[^ ]*)",request_lines[0])
	# file_name=ret.group(1)
	# print("*"*20)
	# print(file_name)
	# print(path+file_name)
	if ret:
		file_name=ret.group(1)
		if file_name=="/":
			file_name="/index.html"
	try:
		f = open(path+file_name,'rb')
		#f= open("./html"+file_name,"rb")
	except:
		response = "HTTP/1.1 404 NOT FOUND\r\n"
		response += "\r\n"
		response+="FILE NOT FOUND\r\n"
		new_client.send(response.encode("utf-8"))
	else:
		html_content=f.read()
		f.close()
		response="HTTP/1.1 200 OK\r\n"
		response+="\r\n"
		new_client.send(response.encode("utf-8"))
		new_client.send(html_content)    		
	#处理请求
	# reponse="HTTP/1.1 200 OK\r\n"
	# reponse+="\r\n"
	# reponse+="hahha"
	#返回请求的数据
	# new_client.send(reponse.encode("utf-8"))
	#关闭
	# new_client.close()

def main():
	#创建套接字
	tcp_service=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#绑定套接字
	tcp_ip=""
	tcp_port=7873
	tcp_addr=(tcp_ip,tcp_port)
	tcp_service.bind(tcp_addr)
	#套接字设置为被动监听
	tcp_service.listen(128)
	#等待用户访问
	new_client,client_addr=tcp_service.accept()
	#执行服务
	service_client(new_client)
	#关闭套接字
	tcp_service.close()

if __name__ == '__main__':
	main()