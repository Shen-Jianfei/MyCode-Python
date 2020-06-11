# 字符串循环左移

s = str(input())
n = int(input())
sstr = s[0:n]
nstr = s + sstr
mstr = nstr[n:]
print(mstr)