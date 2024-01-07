for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    m = {}
    for i in a:
        if i in m:
            m.pop(i)
        else:
            m[i] = 1

    for i in m:
        print(i)