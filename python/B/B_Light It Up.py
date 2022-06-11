# xy 平面上にN 人の人 1,2…Nの1,2,…,N がおり、人 i は座標 (Xi,Yi)にいます。
# このうち、K 人の人 A1,A2,…,Akに同じ強さの明かりを持たせます。
# 座標にいる人が強さR の明かりを持っている時、その明かりによって中心 (x,y) 、半径R の円の内部全体(境界を含む)が照らされます。
# すべての人が少なくとも1 つの明かりによって照らされるために必要な明かりの強さの最小値を求めてください。

import math

N, K = map(int, input().split())
A = list(map(int, input().split()))
l = []
for d in range(N):
    at = list(map(int, input().split()))
    l.append(at)

dif = 0
for d in range(N):
    num = 10000000000000
    for g in range(K):
        div = (l[d][0] - l[A[g]-1][0])**2 + (l[d][1] - l[A[g]-1][1])**2
        if div < num:
            num = div
    if num > dif:
        dif = num


print(math.sqrt(dif))