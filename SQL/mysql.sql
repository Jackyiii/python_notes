--命令
mysql -uroot -p
--退出
exit/quit
--查看数据哭
show databases;
--查看时间
select now();
--查看数据库版本
select version();
--创建数据库
create database Test02 charset=utf8;
--查看如何创建的数据库
show create database Test02;
--删除数据库
drop database Test03;
drop database `python-test01`
--查看当前使用的数据库
select database();
--使用数据库
use database;
--查看数据表
show tables;
--创建表
CREATE TABLE Persons
(
Id_P int,
LastName varchar(255),
FirstName varchar(255),
Address varchar(255),
City varchar(255)
)
;

create table xxx(
id int primary key not null auto_increment,
name varchar(20)
)

create table students(
id int unsigned primary key not null auto_increment,
name varchar(30) not null,
age tinyint unsigned not null,
high decimal(5,2),
gender enum("man","female","double","保密") default "保密",
cls_id int unsigned
)
--查看数据表的结构
desc Persons;

--插入数据
insert into students values(0,"老王",18,18.8,"保密",0);

--查看数据
select * from students;

--修改表的结构
	--增
alter table 表名 add 列表名 类型;
--alter table students add birthday date;
	--删
alter table 表名 drop 列名
	--改
		--重命名版本
alter table 表名 change 原名 新名 类型及约束
		--不重命名版
alter table 表名 modify 列名 类型及约束

#删除数据表
drop table 表名;

#查看创建数据表
show create table students;

--插入
insert into 表名 values(0,"小李",18,17.5,"man","1991-07-27");
insert into 表名 values(default,"小李",18,17.5,"man","1991-07-27");
insert into 表名 values(null,"小李",18,17.5,"man","1991-07-27");

insert 表名 (name,age) values("小巧",16);

insert into 表名 (name,age,gender) values("大乔",17,2),("貂蝉",17,2);

--修改
update 表名 set age=22,gender=2 where id=3;

--条件查询
select * from 表名 where gender="female";
































