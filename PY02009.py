for t in range (int(input())):
    n = int(input())
    a = {}
    for i in range(n):
        num = int(input())
        if num in a:
            a[num] = a[num] + 1
        else:
            a[num] = 1

    max_index = 0
    max_val = 0
    for i in a:
        if a[i] > max_val:
            max_val = a[i]
            max_index = i

        elif a[i] == max_val:
            max_index = min(max_index, i)
    print(max_index)