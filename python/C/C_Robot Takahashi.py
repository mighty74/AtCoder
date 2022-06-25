import bisect
N = int(input())
L = list(input())
W = list(map(int, input().split()))

b = []
s = []

for n in range(N):
    L[n] = int(L[n])
    #print(L[n])
    if L[n] == 1:
        b.append(W[n])
    else:
        s.append(W[n])

b.sort()
s.sort()
count = 0
if len(b) != 0 and len(s) != 0:
    i = bisect.bisect_left(s, b[0])
    count = N - (len(s)-i)
    l = bisect.bisect_right(b, s[len(s)-1])
    countC = N - l
    if count < countC:
        count = countC
else:
    count = N
print(count)