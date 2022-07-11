N, M, X, T, D = map(int, input().split())



if M >= X:
    print(T)
else:
    an = (X - M) * D
    print(T - an)