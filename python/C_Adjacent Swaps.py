n, q = map(int, input().split())

l = []
pos = []
for d in range(n):
    l.append(d+1)
    pos.append(d+1)


for d in range(q):
    a = (int)(input())
    k = pos[a-1]-1
    nk = k
    if n-1 == k:
        nk -= 1
    else:
        nk += 1
    v = l[k]-1
    nv = l[nk]-1
    l[k], l[nk] = l[nk], l[k]
    pos[v], pos[nv] = pos[nv], pos[v]

print(*l)