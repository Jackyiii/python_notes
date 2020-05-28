def PrintLine(char, times):
    print(char * times)


# 点击函数，Insert documentation string sub说明参数的文档注释
def PrintManyLines(char, times, row):
    """
    能够打印row行，times次和char形状的一行线
    :param char: 打印的形状
    :param times: 次数
    :param row: 行数
    """
    i = 0
    while i < row:
        print(char * times)
        i += 1


PrintManyLines("+", 3, 4)
