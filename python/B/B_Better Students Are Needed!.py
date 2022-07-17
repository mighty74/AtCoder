from binascii import a2b_base64
import bisect

N, X, Y, Z = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

AA = sorted(A)



dlist = [0 for n in range(N)]
i = 0

for n in range(N):
    l = AA[N - n - 1]
    if i == X:
        break
    for k in range(N):
        if l == A[k] and dlist[k] == 0:
            dlist[k] += 1
            i += 1
            break
    


BB = sorted(B)




i = 0
for n in range(N):
    l = BB[N - n- 1]
    if i == Y:
        break
    for k in range(N):
        if l == B[k] and dlist[k] == 0:
            dlist[k] += 1
            i += 1
            break

num = []
for n in range(N):
    num.append(A[n] + B[n])


Nnum = sorted(num)

i = 0

for n in range(N):
    l = Nnum[N - n - 1]
    if i == Z:
        break
    for k in range(N):
        if l == num[k] and dlist[k] == 0:
            dlist[k] += 1
            i += 1
            break
    



an = []
for n in range(len(dlist)):
    if dlist[n] == 1:
        an.append(n+1)

print(*an)