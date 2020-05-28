# res=0
# def sum(num):
#     global res
#     res+=num
#     if num == 0:
#         print(res)
#         return res
#     sum(num - 1)
# a=sum(3)

def sum_num(num):
    if num==1:
        return 1
    temp=sum_num(num-1)
    return temp +num
res=sum_num(3)
print(res)