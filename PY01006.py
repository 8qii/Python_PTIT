def check(s):
    for i in range(len(s)):
        if s[i] != '4' and s[i] != '7':
            return "NO"
    return "YES"


for _ in range (int(input())):
    s = input()
    print(check(s))
