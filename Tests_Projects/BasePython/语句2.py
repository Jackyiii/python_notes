#while循环
#break完全结束语句
x=1
while True:
    x += 1
    print(x)
    if x>20:
        break
#else无法与break合用，因为break会跳出包括else的语句
#可以与continue合用，就是不执行while的语句直接转到continu的语句
#多行注释commd+？
for x in "I'm YI FEI, Just cool you konow?".split(" "):
    print(x)
else:
    print(x)
#else会保留最后一个代码块的值
#Bool的惰性求值

True and False and False and True
#只要看到有false就不看其他的了



