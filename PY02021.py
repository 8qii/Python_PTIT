for t in range(int(input())):
    m,n,p = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    res = []
    i = 0
    j = 0
    k = 0
    while True:
        if i == m or j == n or k == p:
            break
        if a[i] == b[j] and b[j] == c[k]:
            res.append(a[i])
            i += 1
            j += 1
            k += 1
            if i == m or j == n or k == p:
                break
            continue
        if a[i] > b[j] :
            j += 1
        elif a[i] < b[j]:
            i += 1
        elif b[j] > c[k]:
            k += 1
        elif b[j] > c[k]:
            j += 1
        elif a[i] < c[k]:
            i += 1
        elif a[i] > c[k]:
            k += 1

    if len(res) == 0 : print("NO")
    else :print(*res, sep = ' ', end = '')
    print()
