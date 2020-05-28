"""
一次只读取一行内容提高效率

"""
file=open("readMe.txt")
while True:
    text=file.readline()
    if not text:
        break
    print(text,end="")
file.close()

