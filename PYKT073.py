lst = []

for kkkk in range(int(input())):
    s = input()
    lst.append(len(list(s.split())))

i = 0

ll = []
cnt = 0

while i < len(lst):
    if lst[i] == 6:
        cnt += 1
        ll.append(1)
        while lst[i] == 6:
            i = i + 2
            if i >= len(lst):
                break

    if i >= len(lst):
        break

    if lst[i] == 7:
        cnt += 1
        ll.append(2)
        i = i + 4

print(cnt)
for i in ll:
    print(i)
