n = int(input()) + 1
a = [int(x) for x in input().split()] + [-1]
ans, x, k = 0, 0, max(a)
for i in range(n):
    if a[i] == k:
        x += 1
    else:
        ans = max(ans, x)
        x = 0
print(ans)
