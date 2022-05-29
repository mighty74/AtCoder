i = list(map(int, input().split()))
l = list(map(int, input().split()))

k = 4
if l[1]==1:
    k -= 1
if l[1]==i[1]:
    k -= 1
if l[0]==1:
    k -= 1
if l[0]==i[0]:
    k -= 1

print(k)