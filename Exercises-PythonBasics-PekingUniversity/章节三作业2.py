# 斜边上的高
import math

a = int(input())
b = int(input())
c = math.sqrt(a ** 2 + b ** 2)
h = (a * b) / c
print(round(h, 2))
