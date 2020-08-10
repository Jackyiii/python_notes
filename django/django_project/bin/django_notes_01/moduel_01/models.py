from django.db import models
#设计和表对应的类，模型类
# Create your models here.

#例如图书类
class BookInfo(models.Model):
	"""图书模型类"""
	#图书名称
	btitle=models.CharField(max_length=20)
	#图书出版日期-日期类型
	bpub_date=models.DateField()


#多类
#英雄人物类
#性别
#年龄
#备注
#关系属性
class HeroInfo(models.Model):
	hname=models.CharField(max_length=20)
	hgender=models.BooleanField(default=False)
	hcomment=models.CharField(max_length=128)
	hbook=models.ForeignKey("BookInfo",on_delete=models.CASCADE)
