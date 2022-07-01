N = int(input())
A = list(map(int, input().split()))
A.sort()
A = list(set(A))

an = 0
if A[0] == 0:
    if len(A) == 1:
        an = 1
    else:
        for n in range(len(A)-1):
            if A[n]+1 == A[n+1]:
                if n == len(A)-2:
                    an = A[n+1]+1
                continue
            else:
                an = A[n]+1
                break
print(an)