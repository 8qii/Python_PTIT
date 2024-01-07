for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    m = []
    for i in a:
        if i in m:
            pass
        else:
            m.append(i)
    print(max(a) - min(a) + 1 - len(m))