for t in range(int(input())):
    n, k = [int(i) for i in input().split()]
    cnt = 0
    for i in range(2, n + 1):
        a = i
        while a % k == 0:
            a = int(a / k)
            cnt += 1
    print(cnt)
