while True:
    s = input()
    if s == '-1':
        break
    l, r = [int(i) for i in s.split()]
    k = int(input())
    max_index = (r + 2) // 2
    min_index = l // k
    a = [0] * (max_index+1) * (k + 1)
    for i in range(2,k+1):
        for j in range(min_index, max_index + 1):
            a[i * j] = 1
    cnt = 0
    for i in range(l, r+1):
        if a[i] == 0: cnt += 1
    print(cnt)