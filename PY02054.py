n, k = [int(i) for i in input().split()]
a = [[0]] * n
for i in range(n):
    a[i] = [int(j) for j in input().split()]

if n == k:
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()


else:
    x = min(n, k)
    res = []

    if n > k:
        drop = n - k
        for i in range(n):
            if i % 2 == 0 and drop > 0:
                drop -= 1
                continue
            tmp = []
            for j in range(k):
                tmp.append(a[i][j])
            res.append(tmp)

    elif k > n:
        for i in range(n):
            tmp = []
            drop = k - n
            for j in range(k):
                if j % 2 == 1 and drop > 0:
                    drop -= 1
                    continue
                tmp.append(a[i][j])
            res.append(tmp)

    for i in range(x):
        for j in range(x):
            print(res[i][j], end = ' ')
        print()