"""
小条件满足条件后使用break

"""
i = 0
while i < 10:
    print(i)
    if i > 5:
        break
    i += 1
print(i)

j = 0
while j < 6:
    if j == 3:
        j += 1
        continue
    print(j)
    j += 1
print(j)
