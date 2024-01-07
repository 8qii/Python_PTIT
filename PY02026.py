def check(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = {}
d = {}
for i in a:
    c[i] = 1
for i in b:
    d[i] = 1

a = sorted(list(c))
b = sorted(list(d))
if check(a, b): print("YES")
else: print("NO")
