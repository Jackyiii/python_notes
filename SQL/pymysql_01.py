#import pymysql;
from pymysql import *


def main():
	#创建Connection对象
	conn=connect(host="localhost",port=3306,user="root",password="072718",database="Data_python01",charset="utf8")
	#获取Cursor对象
	cs1=conn.cursor()
	#执行select语句并且返回受影响行数：查询一条数据
	count=cs1.execute("select * from goods")
	#打印受影响的行数
	print(count)
	for i in range(count):
		#获取查询结果
		#fetchone返回元祖，里面是数据信息
		result =cs1.fetchone() 
		#fetchmany返回一组数据，参数返回个数，元祖的形式
		#result2=cs1.fetchmany(3)
		#fetchall()返回所有数据库数据
		#result3=cs1.fetchall()


		print(result)

	cs1.close()
	conn.close()

if __name__ == '__main__':
	main()