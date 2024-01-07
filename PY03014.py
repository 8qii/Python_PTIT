for t in range(int(input())):
    s = input()
    cnt = 1
    a = []
    for i in s:
        if i == ')':
            print(a[len(a) - 1], end = ' ')
            a.pop()
        elif i == '(':
            print(cnt, end = ' ')
            a.append(cnt)
            cnt += 1
    print()