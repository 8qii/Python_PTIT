def dfs(n):
    vs[n] = True
    for i in l[n]:
        if not vs[i] and i != skip:
            dfs(i)

l = []
skip = 0
vs = []


for t in range(int(input())):
    n, m, p, q = [int(i) for i in input().split()]
    l = []
    for i in range(n+1): l.append([])
    for i in range(m):
        a,b = [int(i) for i in input().split()]
        l[a].append(b)

    cnt = 0
    for i in range(1, n+1):
        if i == p or i == q:
            continue

        else:
            skip = i
            vs = [False] * (n+1)
            dfs(p)
            if vs[q] == False: cnt += 1
    print(cnt)
