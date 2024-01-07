n = int(input())
a,b = [1] * 10001, []
for i in range(2, 10001):
    if a[i] == 1:
        b.append(i)
        for j in range(i * i, 10001, i):
            a[j] = 0

l = [int(i) for i in input().split()]
ans = 0
for i in l:
    s = 100000
    for j in b:
        s = min(s, abs(i-j))
    ans = max(s, ans)
print(ans)
