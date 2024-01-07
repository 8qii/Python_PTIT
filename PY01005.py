t = int(input())
for i in range (0,t):
    s = input()
    dem = 0
    for j in s:
        if j != '4' and j != '7':
            dem += 1

    if dem != 0:
        print('NO')
    else:
        print('YES')
