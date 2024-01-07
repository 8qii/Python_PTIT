vs = []
n = 0
dx = 0
ke = []

def dfs(j):
    for i in ke[j]:
        if vs[i] == 0 and i != dx:
            vs[i] = 1
            dfs(i)

for t in range(int(input())):
    n,m,u,v = [int(i) for i in input().split()]
    vs = [0] * (n + 1)
    for i in range(n+1):
        ke.append([])
    for j in range(m):
        a,b = [int(i) for i in input().split()]
        ke[a].append(b)

    dem = 0
    for i in range(1, n+1):
        if i != u and i != v:
            dx = i
            dfs(u)
            if vs[v] == 0:
                dem += 1
            vs = [0] * (n + 1)
    print(dem)
    ke = []
