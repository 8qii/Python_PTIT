n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a = sorted(a)
cnt = 0
tmp = -999999999
for i in a:
    if i > tmp + k:
        cnt += 1
    tmp = i
print(cnt)