for t in range(int(input())):
    n, c, d = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    a = sorted(a, reverse=True)
    x = min(c,d)
    y = max(c,d)
    res1 = 0
    res2 = 0
    for i in range(x):
        res1 += a[i]
    for i in range(x,x + y):
        res2 += a[i]
    res1 = res1 / x
    res2 = res2 / y
    res = res1 + res2
    print('{:.6f}'.format(res))