#两种方法写出1-10
x=0
# while x<10:
#     x=x+1
#     print(x)
# while True:
#     x=x+1
#     print(x)
#     if x>9:
#         break
# for x in range(1,11):
#     if(x%2==0):
#         continue
#     print(x)
a=[1,2,3,4,5,6]
# for x in a:
#     if(x==8):
#         print("find")
#         break
#     else:
#         print("not find")
#         break
current_a=[]
while a:
    current_a=a.pop()
    print(current_a)
#current_a[-1]=1
print(current_a)