n, k = [int(i) for i in input().split()]
m = []
s = input().split()
for i in s:
    if i not in m:
        m.append(i)
m = sorted(m)
n = len(m)
a = [0] * (k + 1)

def gen(j):
    if j == k:
        for i in range(1, k + 1):
            print(m[a[i]-1], end = ' ')
        print()
        return
    for i in range(a[j] + 1, n + 1 ):
        a[j + 1] = i
        gen(j+1)

gen(0)
