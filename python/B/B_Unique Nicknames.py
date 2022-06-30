N = int(input())
s = []
t = []
an = "Yes"
for n in range(N):
    S, T = map(str, input().split())
    s.append(S)
    t.append(T)

for n in range(N):
    if s[n] == t[n]:
        if s.count(s[n])+t.count(s[n]) != 2 and t.count(t[n])+s.count(t[n]) != 2:
            an = "No"
            break
    else:
        if s.count(s[n])+t.count(s[n]) != 1 and t.count(t[n])+s.count(t[n]) != 1:
            an = "No"
            break

print(an)
