#使用多进程完成服务器
import socket
import re
import multiprocessing
import os
import mini_web
class MSGIServer(object):
	def __init__(self):
		self.tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		self.tcp_server_socket.bind(("",7882))
		self.tcp_server_socket.listen(128)
	def service_client(self,new_socket):
		""" 为这个客户端返回数据 """
		#1.接收浏览器发送过来的请求，即http请求
		#GET / HTTP /1.1
		#...
		request = new_socket.recv(1024).decode("utf-8")
		request_lines=request.splitlines()
		print("")
		print(">"*20)
		print(request_lines)
		file_name=""
		ret=re.match(r"[^/]+(/[^ ]*)",request_lines[0])
		if ret:
			file_name=ret.group(1)
			if file_name=="/":
				file_name="/index.html"
		#如果不是认为是静态资源		
		if not file_name.endswith(".py"):		
			try:
				#f=open("./html"+file_name,"rb")
				path=os.path.expanduser("~/GitProjects/Python/Python/examples_files")+file_name
				f=open(path,"rb")
			except:
				response="HTTP/1.1 404 NOT FOUND\r\n"
				response+="\r\n"
				response+="----file not found"
				#response+=path;
				new_socket.send(response.encode("utf-8"))
	
			else:
				html_content=f.read()
				f.close()
				#2.1 准备发送给浏览器数据--header
				response="HTTP/1.1 200 OK\r\n"
				response+="r\n"
				#准备发送诶浏览器数据
				#response+="hahhaha"
				#将response header发送给浏览器
				new_socket.send(response.encode("utf-8"))
				new_socket.send(html_content)
		else:
			#如果是以py结尾认为是动态资源请求
			header="HTTP/1.1 200 OK\r\n"
			header+="\r\n"
			#body="hhahah"
			#body=login.login()
			body=mini_web.application(file_name)
			response=header+body
			new_socket.send(response.encode("utf-8"))

		new_socket.close()
	
	
	def run_forever(self):
		while True:
			new_socket,client_addr=self.tcp_server_socket.accept()
			p=multiprocessing.Process(target=self.service_client,args=(new_socket,))
			p.start()
			new_socket.close()
		self.tcp_server_socket.close()





def main():
	wsgi_server=MSGIServer()
	wsgi_server.run_forever()


if __name__ == '__main__':
	main()