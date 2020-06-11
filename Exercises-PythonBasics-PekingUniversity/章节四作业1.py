# 合并两个列表并去重

alist=list(map(int,input().split()))
blist=list(map(int,input().split()))
clist = alist + blist
cset = set(clist)
dlist = list(cset)
print(sorted(dlist))