n = int(input())
a = []
for i in range(n) :
    s = input() + ' '
    x = 0
    for i in range(len(s)) :
        if s[i].isdigit() : x = x * 10 + int(s[i])
        else :
            if s[i - 1].isdigit() :
                a.append(x)
                x = 0
for i in sorted(a) : print(i)