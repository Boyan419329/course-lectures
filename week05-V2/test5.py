# 输出1-100之间的前3个偶数

count = 0 #用来计数
i = 0
while i <= 100:
    i = i + 1
    if i % 2 == 0:
        print(i)
        count = count + 1
    if count == 3:
        break
