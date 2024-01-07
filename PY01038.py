for _ in range (int(input())):
    s = input()
    for i in range (1001):
        if int(s) % 7 == 0:
            print(s)
            break
        else :
            s = int(s) + int(s[::-1])
            s = str(s)
        if i == 1000:
            print(-1)
            break