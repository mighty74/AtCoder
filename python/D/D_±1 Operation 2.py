from bisect import bisect_left
N, Q = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
k = []
for n in range(Q):
    num = int(input())
    dif = 0
    for x in range(N):
        dif+=abs(l[x]- num)
    k.append(dif)

for d in k:
    print(d)
