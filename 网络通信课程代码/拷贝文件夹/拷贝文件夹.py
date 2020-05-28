import os
import multiprocessing
def copyFile(q,old_folder_name,new_folder_name,file_name):
	#print("正在从%s--拷贝到--%s-文件名是:%s"%(q,old_folder_name,new_folder_name,file_name))
	old_f=open(old_folder_name+"/"+file_name,"rb")
	content=old_f.read()
	old_f.close()

	new_f=open(new_folder_name+"/"+file_name,"wb")
	new_f.write(content)
	new_f.close()
	#print(old_f)

	#拷贝完成后传入一个消息代表拷贝完
	q.put(file_name)

def main():

	# old_file
	# new_file-
	# list_file-存储所有的文件
	#拷贝文件夹文件到新的文件中

	#1.选择要拷贝的文件
	#old_folder_name=input("请选择要拷贝的文件夹")
	old_folder_name="/Users/Yi/Desktop/网络通信课程代码/拷贝文件夹/test"
	try:
		new_folder_name=old_folder_name+" [copy]"
		os.mkdir(new_folder_name)
	except:
		pass
	#print("正在拷贝文件到 - "+new_folder_name)
	#2.os.listdir()列表列出所有要拷贝的文件的名字
	file_names=os.listdir(old_folder_name)
	#print(file_names)
	#3.通过多任务创建进程池来打开和读取每个文件的内容
	po = multiprocessing.Pool(5)
	q=multiprocessing.Manager().Queue()
	#将进程中添加任务
	for file_name in file_names:
		po.apply_async(copyFile, args=(q,old_folder_name,new_folder_name,file_name))
	#4.创建新的文件夹
	#5.写入到新的文件

	po.close()
	#po.join()
	all_file=len(file_names)
	copy_complet_num=0
	while True:
		file_new=q.get()
		#print("已经完成copy%s"%file_new)
		copy_complet_num+=1
		print("\r拷贝进度: %.2f %% "%(copy_complet_num*100/all_file),end="")
		
		if copy_complet_num>=all_file:
			break
	print()
if __name__ == '__main__':
	main()