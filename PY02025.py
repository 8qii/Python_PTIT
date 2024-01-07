n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = {}
d = {}
for i in a: c[i] = 1
for i in b: d[i] = 1

for i in sorted(list(c)):
    if i in d:
        print(i, end = ' ')
print()

for i in sorted(list(c)):
    if i not in d:
        print(i, end = ' ')
print()

for i in sorted(list(d)):
    if i not in c:
        print(i, end = ' ')