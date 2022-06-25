import string


N, K = map(int, input().split())

k = (K-1) // N
l = list(string.ascii_lowercase)
if k != 0:
    print(str(l[k-1]).upper())
if k == 0:
    print(str(l[k]).upper())