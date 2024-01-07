import math


def check(a, b):
    a = math.gcd(a, b)
    if a == 1:
        return True
    return False


a,b = [int(i) for i in input().split()]
cnt = 0
for _ in range (int(math.pow(10,b-1)) , int(math.pow(10,b))):
    if check(a,_):
        cnt += 1
        if cnt % 10 == 0:
            print(_)
        else :
            print(_, end=' ')


