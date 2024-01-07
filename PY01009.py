s = input()

dl = 0

for i in s:
    if i.islower():
        dl = dl + 1

if dl >= len(s) - dl :
    s = s.lower()
    print(s)

else :
    s = s.upper()
    print(s)
