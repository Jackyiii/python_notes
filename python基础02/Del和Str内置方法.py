class Dogs:
    def __init__(self, _name):
        self.name = _name
        print("%s是不听话的狗" % self.name)

    def __del__(self):
        print("消除")

    def __str__(self):
        n = "内置字符串"
        return n


afu = Dogs("阿福")
print(afu)
del afu
