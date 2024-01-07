while True:
    a = []
    n = (int(input()))
    if n == 0 : break
    if n > 100: n = 100
    for i in range(n):
        a.append(int(input()))
    if min(a) == max(a): print("BANG NHAU")
    else : print(min(a), max(a), sep = ' ')