def check(s):
    n = len(s)
    for i in range (n - 1):
        if int(s[i]) > int(s[i+1]):
            return False
    return True

for _ in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
