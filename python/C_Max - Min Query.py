# 整数の多重集合 S があります。はじめ S は空です。
# Q 個のクエリが与えられるので順に処理してください。 クエリは次の 3 種類のいずれかです。
# 1 x : S に x を 1 個追加する。
# 2 x c : S から x を min(c, (S に含まれる x の個数 )) 個削除する。
# 3 : (S の最大値 )- (S の最小値 ) を出力する。このクエリを処理するとき、 
# S が空でないことが保証される。
import bisect
i = int(input())
l = []
n = []
for k in range(i):
    m = list(map(int, input().split()))
    l.append(m)
    if m[0] == 1:
        n.append(m[1])
Set = set(n)
List = list(Set)
List.sort()
if len(List) != 0:
    Max = List[0]
    Min = List[0]
else:
    Max = -1
    Min = 100000000
an = []

CountList = [0 for k in range(len(List))]

for at in l:
    if at[0] == 1:
        CountList[bisect.bisect_left(List, at[1])] += 1
        if Max < at[1]:
            Max = at[1]
        if Min > at[1]:
            Min = at[1]
    if at[0] == 2:
        point = bisect.bisect_left(List, at[1])
        if len(List) != 0:
            if List[point] != at[1]:
                continue
            if CountList[point] > at[2]:
                CountList[point] -= at[2]
            else:
                CountList[point] = 0
                if List[point] == Max:
                    for d in range(point+1):
                        if CountList[point-d] != 0:
                            Max = List[point-d]
                            #print(List[point-d])
                            break
                if List[point] == Min:
                    for d in range(len(List)-point):
                        if CountList[point+d] != 0:
                            #print(len(List), len(List)-point, d)
                            Min = List[point+d]
                            break
    if at[0] == 3:
        for x in CountList:
            if x != 0:
                an.append(Max - Min)
                break

for answer in an:
    print(answer)
