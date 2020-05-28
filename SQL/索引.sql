#通过特殊信息找到特殊的范围
#为了提高查询的效率
#索引是一种特殊的文件
#InnoDB数据表上的索引是表空间的一个组成部分

create table test_index(title varchar(10));
#时间监测
set profiling=1;
select * from test_index where title="ha-99999";

show profiles;
create index title_index on test_index(title(10));
select * from test_index where title="ha-99999";
