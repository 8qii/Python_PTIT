file = open('DATA.in', 'r')
o = file.read().split('\n')
arr = [int(i) for i in o]
index = 1
for t in range(arr[0]):
    n = arr[index]
    index += 1
    s = str(arr[index])
    index += 1
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
