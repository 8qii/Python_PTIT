n = int(input())
a = []
while True:
    arr = [int(i) for i in input().split()]
    for i in arr:
        a.append(i)
    if len(a) == n: break
b = []
c = []
d = [0] * n
res = []
for i in range(n):
    if a[i] % 2 == 0:
        d[i] = 0
        b.append(a[i])
    else:
        d[i] = 1
        c.append(a[i])


b = sorted(b)
c = sorted(c, reverse = True)
i = 0
j = 0

for k in range(n):
    if d[k] == 0:
        res.append(b[i])
        i += 1
    if d[k] == 1:
        res.append(c[j])
        j += 1

print(*res)