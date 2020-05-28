from pymysql import connect

class JinDo(object):
	def __init__(self):
		self.conn=connect(host="localhost",port=3306,user="root",password="072718",database="Data_python01",charset="utf8")
		#获取Cursor对象
		self.cs1=self.conn.cursor()

	def __del__(self):
		self.cs1.close()
		self.conn.close()

	def execute_sql(self,sql):
		self.cs1.execute(sql)
		for temp in self.cursor.fetchall():
			print(temp)
		#查询部分完成

		#如果想要增删改需要添加一个commit
		#self.conn.commit()

	def show_all_items(self):
		""" 所有商品"""
		sql="select * from goods;"
		self.execute_sql(sql)

	def show_cates(self):
		""" 所有商品"""
		sql="select name from goods_cates;"
		self.execute_sql(sql)

	def show_brands(self):
		sql="select name from goods_brands;"
		self.execute_sql(sql)

	def add_brands(self):
		item_name=input("请输入新商品分类的名称")
		sql="""insert into goods_brands(name) values("%s"); """%item_name
		self.cs1.execute(sql)
		self.conn.commit()

	def get_info_by_name(self):
		find_name=input("请输入商品的名字")
		#sql=""" select * from goods where name ="%s"; """%find 
		sql="select * from goods where name=%s"
		self.cs1.execute(sql,[find_name])
		self.execute_sql(sql)

	@staticmethod
	def print_menu():
		print("——--京东-----")
		print("1.所有的商品")
		print("2.所有的商品分类")
		print("3.所有的商品品牌分类")
		print("4.添加一个商品分类")
		print("5.根据名字查询商品")
		return input("请输入序号")


	def run(self):
		while True:
			num=self.print_menu()
			if num=="1":
				#查询所有商品
				self.show_all_items()
			elif num=="2":
				#查询分类
				self.show_cates()
			elif num=="3":
				#查询品牌分类
				self.show_brands()
			elif num=="4":
				self.add_brands()
			elif num=="5":
				self.get_info_by_name()
			else:
				print("输入有误，请重新输入")



def main():
	#创建京东商城对象
	jd=JinDo()
	#调用对象的run方法让它运行
	jd.run()



if __name__ == '__main__':
	main()