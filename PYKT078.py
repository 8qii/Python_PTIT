for t in range(int(input())):
    n, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    x = max(a)
    for i in range(n):
        if a[i] == x:
            a.insert(i, k)
            break
    b = []
    c = []
    for i in a:
        if i < 0:
            b.append(i)
        else:
            c.append(i)

    for i in b: print(i, end = ' ')
    for i in c: print(i, end = ' ')
    print()