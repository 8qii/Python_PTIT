s = input()
x = input()
n = int(input())
s = s[:n-1] + x + s[n-1:]
print(s)