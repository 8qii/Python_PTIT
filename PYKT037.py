for t in range(int(input())):
    a, b = [int(i) for i in input().split()]
    res = []
    final = []
    while a != 0:
        res.append( a % b )
        a = int(a//b)
    for i in res:
        if i >= 10:
            final.append(chr(ord('A') + (i - 10)))
        else: final.append(str(i))

    res = reversed(final)
    res = ''.join(res)
    print(res)