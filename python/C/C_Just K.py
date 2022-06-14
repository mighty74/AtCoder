from bisect import bisect_left, bisect_right


N, K = map(int, input().split())
l = []
k = []
for n in range(N):
    l.extend(list(input()))

l.sort()
bpos = 0
for i in range(97, 123):
    pos = bisect_right(l, chr(i))
    if pos - bpos >= K:
        k.append(chr(i))
    bpos = pos
    if pos == len(l):
        break

print(len(k))