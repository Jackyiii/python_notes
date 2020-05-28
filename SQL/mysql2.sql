--创建数据库
create database test03 charset=utf8;
--使用数据库
use test03;
--显示当前的数据库
select database();

--create table
create table students(
	id int unsigned primary key auto_increment not null,
	name varchar(20) default '',
	age tinyint unsigned default 0,
	height decimal(5,2),
	gender enum("男","女","保密") default "保密",
	cls_id int unsigned default 0,
	is_delete bit default 0
);
--class 表
create table classes(
	id int unsigned primary key auto_increment not null,
	name varchar(30) not null
);

insert into students values
(0,"小明",18,180.00,2,1,0),
(0,"小月月",19,180.00,2,2,1),
(0,"彭于晏",29,185.00,1,1,0),
(0,"刘德华",18,180.00,1,2,1),
(0,"小乔",18,180.00,2,1,0),
(0,"大乔",18,180.00,2,2,1),
(0,"曹操",18,180.00,2,1,1),
(0,"刘备",18,180.00,1,1,0),
(0,"张飞",18,180.00,2,2,0),
(0,"诸葛亮",18,180.00,2,3,1),
(0,"流动",18,180.00,2,1,0),
(0,"里那个",18,180.00,2,4,0),
(0,"李娜",18,180.00,1,4,0),
(0,"曹丕",18,180.00,2,1,0),
(0,"马超",18,180.00,2,5,0)

insert into classes values(0,"python_01"),(0,"python_02");



--查询指定字段
-- select 1,2 from 表名;
select name age from students;
--使用as给字段起名字
select name as 姓名,age as 年龄 from students;
--select 表名.字段 from 表名;
select  students.name, students.age from students;

--as给表起名字
select s.name,s.age from stduents as s;	
--去重
select distinct gender from students;
--查询大于18的信息
select * from students where age>18;
--查询小于18的信息
select * from students where age<18;
--查询所有年龄为18的学生
select * from students where age=18;
select id,name,gender from students where age>18;
--and
--18-20所有信息
select * from students where age>18 and age<28;
select * from students where age>18 and gender=2;
--or
--18以上或者身高高于180以上的
select * from students where  age>18 or height>180;
--not
select * from students where not (age>18 and gender=2);
select * from students where (not age>18) and gender=2;

--模糊查询
--like 
--%替换1个或者多个
--_替换一个
--查询姓名中以小开头的名字
select name from students where name like "小%";
select name from students where name like "%小%";
--查询姓名中 2个字的
select name from students where name like "___";
--查询至少有两个字的名字
select name from students where name like "__%";
--查询姓名中 3个字的
select name from students where name like "__";

--rlike正则
--查询以周开始的名字
 select name from students where name rlike "^周.*";
 --查询以周开始轮结尾的名字
 select name from students where name rlike "^周.*伦$";

select name from students where age in(18,20,34);
select name age from students where age not in(19,29);
select name age  from students where age between 18 and 20;
select name age from students where age not between 18 and 33;

select * from students where height is not null;
--排序
--18-34之间男性 排序
--asc从小到大，desc从大到小
select * from students where (age between 18 and 34) and gender=1 order by age asc;
select * from students where (height between 160 and 180) and gender=2 order by height asc,id desc;
--查询男性有多少个人
select count(*) as 男性人数 from students where gender=1;
select count(*) as 男性人数 from students where gender=2;
select count(*) as 总人数 from students 

--求最大值
select max(age) as 男性年龄最大值 from students;

--sum
select sum(age) as 总和 from students;

select avg(age) from students;

select sum(age)/count(*) students;
select round (sum(age)/count(*),2) from students;
select round(avg(height),2) from students;
--group by分组
select gender from students group by gender;
select gender,count(*) from students group by gender;
select gender,group_concat(name) from students group by gender;
--having
--查询平均年龄超过30岁的性别，姓名 having avg(age)>30
select gender, group_concat(name) from students group by having avg(age)>30;

--limit分页
select * from students limit 0,5;
select * from students limit 5,5;
select * from students where gender=1 limit 2;
--每页2个，第一页
select * from students limit 0,2;
--每页2个，第2页
select * from students limit 2,2;
--每页2个，第3页
select * from students limit 4,2;
--limit (第n页-1)*每页个数,每页个数
select * from students order by age asc limit 10,2;

--选择所有女性，身高排序只显示两个
select * from students where gender=2 order by height desc limit 2;
--链接
--查询能够对应班级的学生的信息
select * from students inner join classes on students.cls_id=classes.cls_id;
--条件相同但只显示姓名和班级
select students.*,classes.name from students inner join classes on students.cls_id=classes.cls_id;
select students.name,classes.name from studnets inner join classes on students.cls_id=classes.cls_id;
select from s.name,c.name students as s inner join classes as c on s.cls_id=c.cls_id;

--左链接，以左边的表为主  --以student的数据为主
select * from students as s left join classes as c on s.cls_id=c.id;

--原表里选用where ，结果里选用having


























