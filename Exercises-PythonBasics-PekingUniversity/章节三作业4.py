# 计算字符个数

s = str(input())
ss = s.split(' ')
fs = ss[0]
ls = ss[-1]
n = 0
for i in fs:
    if i in ls:
        n = n + 1
    else:
        n = n
print(n)