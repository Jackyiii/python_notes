a = 10


def demo1():
    return a + 10


class Dog:
    def __init__(self, name):
        self.name = name

    def play(self):
        print("%s,在玩" % (self.name))
