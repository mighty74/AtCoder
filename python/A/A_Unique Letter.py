N = input()
S = list(N)
an = []

if S.count(S[0]) == 1:
    an.append(S[0])
if S.count(S[1]) == 1:
    an.append(S[1])
if S.count(S[2]) == 1:
    an.append(S[2])

if len(an) == 0:
    print('-1')
else:
    print(an[0])