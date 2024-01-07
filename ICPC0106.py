for t in range(int(input())):
    n = int(input())
    s = input()
    s = s[::-1]
    res = 0
    for i in range(len(s)):
        res += int(s[i]) * (2 ** i)
    ans = ''
    while res > 0:
        tmp = res % n
        if tmp >= 10:
            tmp = chr(ord('A') + (tmp - 10))
        ans += str(tmp)
        res = res // n
    ans = ans[::-1]
    print(ans)
