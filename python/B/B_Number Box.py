N = int(input())
L = []
for n in range(N):
    L.append(list(map(int, input())))
bmax = 0
Bpos = []
for n in range(N):
    for k in range(N):
        if bmax <= L[n][k]:
            if bmax == L[n][k]:
                Bpos.append([n,k])
            else:
                Bpos = []
                Bpos.append([n,k])
                bmax = L[n][k]
smax = 0
Spos = []
if N > 1:
    for n in Bpos:
        for k in range(-1, 2):
            for l in range(-1, 2):
                if k == 0 and l == 0:
                    continue
                else:
                    x = n[0]+k
                    y = n[1]+l
                    if x >= N:
                        x = n[0]-N+k
                    if y >= N:
                        y = n[1]+l-N
                    if x < 0:
                        x = n[0]+N+k
                    if y < 0:
                        y = n[1]+l+N
                    if x < N and y < N:
                        if smax <= L[x][y]:
                            if smax == L[x][y]:
                                Spos.append([x,y, k, l])
                            else:
                                Spos = []
                                Spos.append([x,y, k, l])
                                smax = L[x][y]
                    else:
                        if smax <= L[x][y]:
                            if smax == L[x-N][y-N]:
                                Spos.append([x,y, k, l])
                            else:
                                Spos = []
                                Spos.append([x,y, k, l])
                                smax = L[x][y]
d = []
if N > 2:
    num = []
    for n in Spos:
        at = 0
        for k in range(N-2):
            x = n[0]+n[2]*(k+1)
            y = n[1]+n[3]*(k+1)
            if x >= N:
                x = x - N
            if y >= N:
                y = y - N
            if x < 0:
                x = N + x
            if y < 0:
                y = N + y
            ate = 1
            for i in range(N-3-k):
                ate *= 10
            at += L[x % N][y % N] * ate
        d.append(at)

print(bmax, end='')
print(smax, end='')
if len(d) != 0:
    answer = max(d)
    print(answer)


