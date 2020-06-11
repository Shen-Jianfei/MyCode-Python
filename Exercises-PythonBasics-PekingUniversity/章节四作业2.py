# 对列表元素进行分类后加标签存入字典。

# 输入一个列表，要求列表中的每个元素都为正整数且列表包含的元素个数为偶数；
# 将列表中前一半元素保存至字典的第一个键值1中，后一半元素保存至第二个键值2中。

alist = list(map(int, input().split()))
n = len(alist)
clist = alist[:int(n/2)]
dlist = alist[int(n/2):]
adict = {'1':clist, '2':dlist}
print(adict)