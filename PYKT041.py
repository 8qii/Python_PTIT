def calc(num):
    return int(num * (num - 1) / 2)

n = int(input())
a = []
for i in range(n):
    s = input()
    tmp = []
    for c in s:
        if c == 'C':
            tmp.append(1)
        else: tmp.append(0)
    a.append(tmp)

cap = 0

for i in range(n):
    if sum(a[i]) >= 2:
        cap += calc(sum(a[i]))

for i in range(n):
    tong = 0
    for j in range(n):
        tong += a[j][i]
    if tong >= 2:
        cap += calc(tong)

print(cap)
