i = int(input())

an = [[] for d in range(i)]
for k in  range(i):
    for d in  range(k+1):
        if d == 0 or d == k:
            an[k].append(1)
        elif len(an[k-1]) > d:
            an[k].append(an[k-1][d] + an[k-1][d-1])
for k in an:
    for d in range(len(k)):
        if d == len(k)-1:
            print(k[d])
        else:
            print(k[d],end=" ")

