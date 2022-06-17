import collections

N = int(input())
S = [[] for i in range(10)]
for n in range(N):
    l = list(map(int, input()))
    count = 0
    for k in l:
        S[k].append(count)
        count += 1

an = []

for i in range(10):
    Max = 0
    at = S[i]
    at.sort()
    numlist = []
    for k in range(10):
        numlist.append(at.count(k))
    Max = max(numlist)
    poslist = []
    for k in range(10):
        if numlist[k] == Max:
            poslist.append(k)
    pos = poslist[len(poslist)-1]
    an.append((Max-1) * 10 + pos)
#print(an)
print(min(an))
