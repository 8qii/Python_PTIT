import math

for _ in range (int(input())):
    a , b, c = [float(i) for i in input().split()]
    res = math.log(c/a , 1 + b/100)
    print(math.ceil(res))