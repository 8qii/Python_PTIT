for t in range(int(input())):
    arr = [int(i) for i in input().split()]
    n = arr[1]
    res = arr[0]
    ans = ''
    while res > 0:
        tmp = res % n
        if tmp >= 10:
            tmp = chr(ord('A') + (tmp - 10))
        ans += str(tmp)
        res = res // n
    ans = ans[::-1]
    print(ans)
