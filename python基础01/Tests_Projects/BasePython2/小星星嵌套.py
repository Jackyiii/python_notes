# print("*",end="") =>不会换行
i = 0
j = 0
s = "*"
while i < 5:
    print(s * (i + 1))
    i += 1

k = 0

s = "#"
while k < 5:

    l = 0
    while l <= k:
        print(s, end="")
        l += 1
    print("")
    k += 1
