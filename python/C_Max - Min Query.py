# 整数の多重集合 S があります。はじめ S は空です。
# Q 個のクエリが与えられるので順に処理してください。 クエリは次の 3 種類のいずれかです。
# 1 x : S に x を 1 個追加する。
# 2 x c : S から x を min(c, (S に含まれる x の個数 )) 個削除する。
# 3 : (S の最大値 )- (S の最小値 ) を出力する。このクエリを処理するとき、 
# S が空でないことが保証される。


i = int(input())
l = []
an = []
for k in range(i):
    m = list(map(int, input().split()))
    if m[0] == 1:
        l.append(m[1])
    if m[0] == 2:
        for g in range(m[2]):
            if m[1] in l: 
                l.remove(m[1])
    if m[0] == 3:
        if len(l) != 1 and len(l) != 0:
            an.append(max(l) - min(l))

for answer in an:
    print(answer)
