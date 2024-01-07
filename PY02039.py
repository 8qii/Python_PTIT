n = int(input())
a = [[]] * n
for i in range (n):
    a[i] = [int(j) for j in input().split()]

k = int(input())

s1 = 0
s2 = 0

for i in range (n):
    for j in range (n):
        if i > j:
            s1 += a[i][j]
        elif j > i:
            s2 += a[i][j]

if abs(s1 - s2) > k:
    print("NO")
    print(abs(s1 - s2))
else:
    print("YES")
    print(abs(s1 - s2))