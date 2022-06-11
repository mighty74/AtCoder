#整数X が与えられます。このX に以下を施すことを「操作」と呼びます。
#操作の内容
# Xに1加算
# Xに1減算
#初項 A 、公差 D 、項数 N の等差数列 S に含まれる数を「良い数」と呼びます。
#「操作」を 0 回以上何度でも使って X を「良い数」にする時、必要な「操作」の最小回数を求めてください。


X, A, D, N = map(int, input().split())
dif = 0
if D > 0:
    if A > X:
        dif = abs(A - X)
    elif A + D * (N-1) < X:
        dif = abs(X - (A + D * (N-1)))
    else:
        at = abs(X - A) // abs(D)
        next = at + 1
        if at+1 != N:
            dif = abs(X - (A + D * at))
            dif1 = abs(X - (A + D * next))
            if dif > dif1:
                dif = dif1
        else:
            dif = abs(X - (A + D * at))

elif D < 0:
    if A < X:
        dif = abs(A - X)
    elif A + D * (N-1) > X:
        dif = abs(X - (A + D * (N-1)))
    else:
        at = abs(A - X) // abs(D)
        next = at + 1
        if at+1 != N:
            dif = abs(X - (A + D * at))
            dif1 = abs(X - (A + D * next))
            if dif > dif1:
                dif = dif1
        else:
            dif = abs(X - (A + D * at))
else:
    dif = abs(A - X)

print(dif)
