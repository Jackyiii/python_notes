#视图
#虚拟的表
#提高了重用性，像一个函数
#数据库重构，却不影响程序的运行
#提高了安全性，可以对不同用户
#让数据更加清晰
create view v_goods_info as select g.*, 
				  c.name as cate_name,
				  b.name as brand_name 
				  from goods as g 
				  left join goods_cates as c 
				  on g.cate_id=c.id 
				  left join goods_brands as b 
				  on g.brand_id=b.id;
