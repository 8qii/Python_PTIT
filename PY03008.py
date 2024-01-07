n = int(input())
l = [0] * (n+1)
for t in range (n - 1):
    a,b = [int(i) for i in input().split()]
    l[b] += 1
    l[a] += 1

bool = True

for i in range(1, n+1):
    if l[i] != 1 and l[i] != n-1:
        print("No")
        bool = False
        break

if bool:
    print("Yes")

