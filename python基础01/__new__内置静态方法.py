"""
类名创建对象-解释器做2件事情，1分配空间 2初始化对象
为内存分配空间使用的方法是__new__方法
__new__ 返回对象的引用-返回给解释器，解释器-传递到初始化的第一个参数
__new__ return super().__new__(cls)
"""
class MusicPlayer(object):
    instance=None
    def __new__(cls, *args, **kwargs):
        # 创建对象时new方法会自动被调用
        print("创建对象分配空间")
        cls.instance= super().__new__(cls)
        return cls.instance

    #因为默认的父类object的new方法可以实现为对象分配空间
    #所以应该调用父类objectnew 方法
    #new必须返回对象的引用
    def __init__(self):
        print("播放器初始化")

player=MusicPlayer()
print(player)
print(MusicPlayer.instance)
