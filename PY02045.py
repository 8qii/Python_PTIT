def solve(s):
    n = len(s) // 2
    s = str(int(s[:n]) + int(s[n:]))
    print(s)
    if len(s) > 1:
        solve(s)

s = input()
solve(s)