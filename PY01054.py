for _ in range (int(input())):
    s = input()
    res = 1
    for i in s:
        tmp = int(i)
        if tmp != 0:
            res *= tmp

    print(res)