"""
计算0-100偶数的结果

"""
result = 0
i = 0
while i <= 100:
    result += i
    i += 2
    print("i=%d,result=%d" % (i, result))
print(result)
