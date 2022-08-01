
N, A, B = map(int, input().split())

i = N // A
l = 0
if A <= B:
    if i != 0:
        l = (A - 1) * (i - 1)
    else:
        l = 0
elif A > B:
    if i != 0:
        l = (i - 1) * (B - 1)
    else:
        l = 0
k = N % A
d = 0
if i != 0:
    if k >= B:
        d = B - 1
    else:
        d = k
else:
    d = 0

print(l + d + i)
