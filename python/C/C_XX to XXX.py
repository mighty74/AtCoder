S = list(input())
T = list(input())

an = "No"
Snum = [1]
Scat = [S[0]]
Tnum = [1]
Tcat = [T[0]]
for n in range(1, len(S)):
    if S[n] != S[n-1]:
        Snum.append(1)
        Scat.append(S[n])
    else:
        Snum[len(Snum)-1] += 1

for n in range(1, len(T)):
    if T[n] != T[n-1]:
        Tnum.append(1)
        Tcat.append(T[n])
    else:
        Tnum[len(Tnum)-1] += 1

if Scat == Tcat:
    k = True
    for n in range(len(Snum)):
        if Snum[n] > Tnum[n]:
            k = False
            break
        if Snum[n] != Tnum[n]:
            if Snum[n] == 1:
                k = False
                break
    
    if k:
        an = "Yes"


print(an)

