for t in range(int(input())):
    a = input().split(".")
    ok = True
    if len(a) < 4 : ok = False
    for i in a:
        if i.isdigit():
            if int(i) < 0 or int(i) > 255: ok = False
        else: ok = False

    if ok:
        print("YES")
    else:
        print("NO")
