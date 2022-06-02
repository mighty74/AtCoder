from itertools import count


i = list(map(int, input().split()))

f = i[0]
goal = i[1]
seki = i[2]
count = 0
flag = True
while flag:
    if f >= goal:
        flag = False
        break
    f *= seki
    count += 1
print(count)