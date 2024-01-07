def dfs(j):
    for i in ke[j]:
        if not vs[i] and i != key:
            vs[i] = True
            dfs(i)

ke = []
vs = []
n = 0
key = 0


for t in range(int(input())):
    ke = []
    vs = []
    key = 0
    n, k = [int(i) for i in input().split()]
    for i in range(n+1):
        ke.append([])
        vs.append(False)
    for i in range(k):
        x, y = [int(i) for i in input().split()]
        ke[x].append(y)
        ke[y].append(x)

    res = 0
    val = 0
    tplt = 0

    for i in range(1, n+1):
        if not vs[i]:
            dfs(i)
            tplt += 1

    for i in range(1, n+1):
        for m in range(n + 1):
            vs[m] = False
        key = i
        tp = 0
        for j in range(1,n+1):
            if not vs[j] and j != i:
                dfs(j)
                tp += 1
        if tp > val and tp > tplt:
            val = tplt
            res = i

    print(res)