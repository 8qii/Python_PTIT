def check(s):
    if len(s) % 2 == 0:
        return "NO"
    if s[0] == s[1] :
        return "NO"
    x = s[0]
    for i in range (len(s)):
        if i % 2 == 0:
            if s[i] != x:
                return "NO"
    return "YES"


for t in range (int(input())):
    s = input()
    print(check(s))
