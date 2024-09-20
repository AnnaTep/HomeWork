import random

n1 = random.randint(3, 20)
print("Выпало число:", n1)
l = []
for a in range(1, n1 // 2 + 1):
    if a <= n1 // 2:
        for b in range(a + 1, n1):
            if n1 % (a + b) == 0:
                l.append(a)
                l.append(b)
            else:
                continue
    else:
        continue
print(l)
