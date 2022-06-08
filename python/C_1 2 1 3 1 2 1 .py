n = int(input())

s = [1]
l = [1]

for k in range(n):
    if k != 0:
        l = s + [k+1] + s
        s = l.copy()


print(*l)