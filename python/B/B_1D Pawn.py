
N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for i in L:
    if A[i-1] != N:
        if i == K:
            A[i-1] += 1
        else:
            if A[i-1]+1 != A[i]:
                A[i-1] += 1
print(*A)