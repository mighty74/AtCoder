N = int(input())
S = list(input())

an = "Yes"
for n in range(N//2):
    if S[n] == S[N-1-n]:
        if S[n] == "A":
            break
        continue
    else:
        if S[n] == "A":
            if n != 0:
                if S[n-1] == "B":
                    S[N-1-n] = "A"
                    continue
                elif S[n-1] == "A":
                    S[n-1] = "B"
                    continue
            else:
                an = "No"
                break
        elif S[n] == "B":
            if n+1 != N-1-n:
                S[n] = "A"
                S[n+1] = "B"
            else:
                an = "No"
                break

print(an)