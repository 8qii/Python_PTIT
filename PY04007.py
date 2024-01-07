for t in range (int(input())):
    a, b = [int(i) for i in input().split()]
    m = [[0] * b] * a
    for i in range(a):
        m[i] = [int(k) for k in input().split()]

    res = [[0] * a] * a

    for i in range (a):
        for j in range (a):
            res[i][j] = 0
            for k in range (b):
                res[i][j] += m[i][k] * m[j][k]

    for i in range (a):
        for j in range (a):
            print(res[i][j], end = ' ')
        print()

'''
1 2
3 4

1 3
2 4

0 0
0 0

1 * 1 + 2 * 2   1 * 3 + 2 * 4
'''