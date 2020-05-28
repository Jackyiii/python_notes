import random
computer=random.randint(1,3)
player=int(input("石头=1,剪刀=2,布=3"))
print("玩家输入的是%s,电脑输入的是%s"%(player,computer))
if((player==1 and computer==2)
        or (player==2 and computer==3)
        or(player==3 and computer==1)):
    print("玩家赢了")
elif player==computer:
    print("平局")
else:
    print("电脑赢了")