"""
%s 字符串
%d 有符号十进制整数  %06d整数显示位数，不足的地方使用0补全
%f浮点数，%.02f表示小数点后面显示两位
%%输出显示%
"""
name="电电"
print("我的名字叫%s，请多多关照"% name)
num=12
print("我的学号是%06d" % num)
price=9.0
weight=5.0
money=45.0
print("苹果的单价是%.2f元/斤，购买了%.01f斤，需要支付%.02f元"%(price,weight,money))
scale=0.25
print("数据比例是%.2f%%" % (scale*100))