n = input()
cnt = 0
while True:
    cnt += 1
    tong = 0
    for i in n:
        tong += ord(i) - ord('0')
        n = str(tong)
    if len(n) == 1:
        break

print(cnt)