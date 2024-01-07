for t in range(int(input())):
    b = int(input())
    cnt = 0
    for i in range(1,b,1):
        if (i + 1) * (i + 2) / 2 > b + 10: break
        a = b/(i + 1) - i / 2
        if int(a) == a and a > 0:
            # print(i)
            cnt += 1
    print(cnt)
