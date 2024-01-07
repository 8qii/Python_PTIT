n = int(input())
res = 100000000
key = 0
a = [int(i) for i in input().split()]
for i in a:
    tong = 0
    for j in a:
        if j == i:
            continue
        else: tong += abs(i - j)
    if tong < res:
        res = tong
        key = i

print(res, key, sep = ' ')
