import copy
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

str = "Yes"
l = [A[0], B[0]]
for n in range(N-1):
    d = copy.copy(l)
    l = []
    count = 0
    for k in d:
        #print(k)
        if abs(A[n+1] - k) <= K:
            l.append(A[n+1])
        if abs(B[n+1] - k) <= K:
            l.append(B[n+1])
        if abs(A[n+1] - k) > K and abs(B[n+1] - k) > K:
            count += 1
    if count == len(d):
        str = "No"
        break
    
    l = list(set(l))
print(str)
