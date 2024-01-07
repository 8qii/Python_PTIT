for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    cnt = 0
    for i in range(n-1):
        x = max(a[i], a[i+1])
        y = min(a[i], a[i+1])
        if y == x:
            continue
        while y < x:
            cnt += 1
            y = y * 2
        cnt -= 1
    print(cnt)