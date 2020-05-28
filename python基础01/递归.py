def demo(num):
    if num==0:
        return
    print(num)
    demo(num-1)
demo(3)