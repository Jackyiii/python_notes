start transaction; #begin;

	
commit;
rollback;#回滚

#原子性 - 成功或者不成功
#一致性 - 例如转账不会出现其他的情况
#隔离性 - 如果两个客户端对同一个操作其中一个修改数据，另一个只有提交才能完成-如同多线程的锁
#持久性 - 数据库的数据不会因为系统挂了而消失
