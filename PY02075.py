class pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y


for t in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        m, n = [int(i) for i in input().split()]
        x = pair(m, n)
        a.append(x)

    a = sorted(a, key = lambda l : (l.y, -l.x) )

    cnt = 0
    tmp = -1

    for i in a:
        if i.x >= tmp:
            cnt += 1
            tmp = i.y

    print(cnt)