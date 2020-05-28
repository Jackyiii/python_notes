def PrintLine(char, times):
    print(char * times)


def PrintMultiLine(char, times, row):
    """

    :param char: 形状
    :param times: 次数
    :param row: 行数
    """
    i = 0
    while i < row:
        PrintLine(char, times)
        i+=1
name="测试"

#pyc字节码文件，二进制文件，引入包是引入的二进制文件，为了提高性能
