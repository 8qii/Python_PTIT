a = []
b = []
c = []
n = int(input())
cnt = 0
while True:
    k = list(int(i) for i in input().split())


    for i in k:
        if i % 2 == 0:
            c.append(1)
            a.append(i)
        else:
            c.append(0)
            b.append(i)
    cnt += len(k)
    if cnt == n:
        break

a.sort()
b.sort()
b = b[::-1]
r = 0
l = 0
res = []
for i in range (n):
    if c[i] == 1:
        res.append(a[r])
        r += 1

    else :
        res.append(b[l])
        l += 1

for i in res:
    print(i , end = ' ')