create table goods(
	id int unsigned primary key auto_increment not null,
	name varchar(150) not null,
	cate_name varchar(40) not null,
	brand_name varchar(40) not null,
	price decimal(10,3) not null default 0,
	is_show bit not null default 0,
	is_saleoff bit not null default 0
)
#如果是主键 null 0都可以 如果不是，则不能
#删除
#drop table good;
#select * from goods;
#查询cate_name 为超级本的所有信息
#select * from goods where cate_name="超级本";
#..
#select name as 商品名称, price as 商品价格 from goods where cate_name="超级本";
#显示商品的种类
select cate_name from goods group by cate_name;
select distinct cate_name from goods;

select cate_name, group_concat(name) from goods group by cate_name;
#求所有电脑产品的平均价格并且保留两位小数
select round(avg(price),2) as avg_price from goods;
#显示每种商品的平均价格
select cate_name,avg(price) from goods group by cate_name;
#查询每种类型的商品中最贵，最便宜，平均，数量
select cate_name,max(price),min(price),avg(price),count(*) from goods group by cate_name;
#查询所有价格大于平均价格的商品，并且按价格降序排序
select id,name,price from goods where price>(select round(avg(price),2) as avg_price from goods) order by price desc;
#查询每种类型中最贵的电脑信息
select * from goods inner join
(
	select
	cate_name,
	max(price) as max_price,
	min(price) as min_price,
	avg(price) as avg_price,
	count(*) from goods group by cate_name
) as new_goods
on goods.cate_name=new_goods.cate_name and goods.price=new_goods.max_price;

#查询所有价格大于平均价格的商品，并且按价格降序排序
#查询每种类型中最贵的电脑的信息

#----------------------------------------------
#分表
create table if not exists goods_cates(
	id int unsigned primary key auto_increment,
	name varchar(40) not null,
);
select * from goods_cates group by goods_cates;

intert into goods_cates (name) select cate_name from goods group by cate_name;

#同步数据
update goods as g inner join goods_cates as gc on g.cate_name=gc.cate_name set g.cate_name=gc.id;

#修改表-修改字段 重命名版
alter table 表名 change 原名 新名 类型及约束
alter table students change birthday birth datetime not null;
#修改表-修改字段 不重命名版
alter table 表名 modify 列名 类型及约束;
alter table students modify birth date not null;
#关联-外键
alter table goods add foreign key(cate_id) references goods_cates(id);
#-------拆品牌

create table if not exists goods_brands(
	id int unsigned primary key auto_increment;
	name varchar(40) not null,
)
intert into goods_brands (name) select brand_name from goods group by brand_name;
update goods as g inner join goods_brands as gb on g.brand_name=gb.brand_name set g.brand_name=gb.id;
alter table goods add foreign key(brand_id) references goods_brands(id);


#创建表+插入数据
create table goods_brands(
	id int unsigned primary key auto_increment;
	name varchar(40) not null
	)select brand_name as name from goods group by brand_name; 
update goods as g inner join goods_brands as b on g.brand_name=b.name set g.brand_name =b.id;
alter table goods
	change cate_name cate_id int unsigned not null,
	change brand_name brand_id int unsigned not null;

insert into goods_cates(name) values("路由"),("交换机"),("网卡");
insert into goods_brands(name) values("海尔"),("清华方舟"),("神州");

alter table goods add foreign key (brand_id) references goods_brands(id);

#取消外键的
alter table goods drop foreign key 外键名称;







