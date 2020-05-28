file1=open("readMe.txt","r")
file2=open("readMe2.txt","w")
while True:
    text=file1.readline()
    file2.writelines(text)
    if not text:
        break
file1.close()
file2.close()