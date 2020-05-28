import pygame

"""
坐标系的原点在左上角
描述矩形区域的类pygame.Rect(x,y,width,height)
pygame内部属性，x,y,left,top,bottom,right,center,centerx,centery,size,width,height
size return 元祖,第一个值是宽度，第二个值是高度
heroRect=pygame.Rect(100,500,120,125)
print("英雄的原点坐标是%d,%d"%(heroRect.x,heroRect.y)
print("英雄模型的尺寸%d,%d"%(heroRect.width,heroRect.height))
print("%d,%d"%heroRect.size)

pygame.display用于创建管理游戏的窗口
pygame.display.setmode(resolution=(0,0),floags=0,depth=0)返回surface-创建出来的游戏屏幕的大小
resolution指定屏幕的宽高
flags参数指定屏幕的附加选项，是否全屏
depth代表颜色的未数
"""
# 初始化方法
pygame.init()
# 创建游戏的窗口
display = pygame.display.set_mode((480, 700))
# 绘制背景图像
# 加载图像数据
bgImg = pygame.image.load("./images/bg.png")
display.blit(bgImg, (0, 0))
# 更新屏幕的显示
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()
heroRect=pygame.Rect(150,300,102,126)
# 编写游戏代码
while True:
    clock.tick(1)
    #修改飞机的位置
    heroRect.y-=50
    #调用blit绘制图像
    display.blit(heroRect)
    #update显示更新
# 卸载内存和模块
pygame.quit()
