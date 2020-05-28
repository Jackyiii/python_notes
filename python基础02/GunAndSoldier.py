class Gun:
    def __init__(self, model):
        self.model = model
        self.bulletCount = 0

    def addBullet(self, count):
        self.bulletCount += count

    def shoot(self):
        # 判断子弹数量
        if self.bulletCount <= 0:
            print("[%s]没有子弹了" % self.model)
            return
        # 发射子弹
        # 子弹数量减少
        self.bulletCount -= 1
        # 提示发射信息
        print("[%s]发射成功%d" % (self.model, self.bulletCount))


class Soldier:
    def __init__(self, name):
        # 新兵的姓名，枪的属性
        self.name = name
        self.gun = None

    def fire(self):
        # 判断是否有枪
        # 装填子弹
        # 发射子弹
        if self.gun is None:
            print("[%s]没有枪" % self.name)
            return
        print("冲啊%s" % self.name)
        self.gun.addBullet(50)
        self.gun.shoot()


ak47 = Gun("ak47")
ak47.addBullet(50)
ak47.shoot()
xuSan = Soldier("许三多")
xuSan.gun = ak47
xuSan.fire()
print(xuSan.gun)
