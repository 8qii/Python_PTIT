
for t in range(int(input())):
    s = input()
    ss = input()
    s = sorted(s)
    ss = sorted(ss)
    if s == ss:
        print("Test " + str(t+1) + ": YES")
    else:
        print("Test " + str(t+1) + ": NO")
