num = int(input('Number:'))
l = []
for i in range(num):
    if i == 0:
        continue
    if i + num / 2 < num:
        p = i + (num - i)
        if p == num:
            l.append(i)
            l.append(num - i)
    else:
        continue
print(l)
