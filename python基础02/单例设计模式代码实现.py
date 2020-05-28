class Music:
    # 记录第一个被创建对象的引用
    instance = None
    # 记录初始化动作
    initFlag = False

    def __new__(cls, *args, **kwargs):
        # 判断类属性是否是空对象 如果是第一个对象没有被创建
        if cls.instance is None:
            # 没有被创建，应该父类方法为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 返回类属性的保存的对象的引用
        return cls.instance

    def __init__(self):
        # 判断是否执行过初始化动作
        if Music.initFlag:
            return

        # 没有执行再执行初始化动作
        print("初始化播放器")
        # 修改类属性的标记
        Music.initFlag = True


p1 = Music()
p2 = Music()
print(p1)
print(p2)
