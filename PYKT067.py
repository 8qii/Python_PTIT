def Try(j):
    for i in range(1,n + 1):
        if not vs[i]:
            vs[i] = True
            a[j] = str(i)
            if j == n-1:
                res.append(''.join(a))
            else: Try(j + 1)
            vs[i] = False

a = []
vs = []
n = 0
res = []

for t in range(int(input())):
    n = int(input())
    a = ['0'] * n
    res = []
    vs = [False] * (n + 1)
    Try(0)
    print(len(res))
    for i in range(len(res) - 1, -1, -1):
        print(res[i], end = ' ')
    print()