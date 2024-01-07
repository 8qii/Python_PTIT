for t in range(int(input())):
    s = input()
    res = ""
    tong = 0
    for i in s:
        if i.isdigit():
            tong += int(i)
        else: res += i
    res = sorted(res)
    print("".join(res), tong, sep = "")