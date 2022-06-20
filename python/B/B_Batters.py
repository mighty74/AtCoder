N = int(input())

l = list(map(int, input().split()))
an = l.copy()
for k in range(N):
    for d in range(N-k-1):
        an[k] += l[k+d+1]
count = 0
for k in an:
    if k < 4:
        count +=1

print(N-count)