# 整数R,C と 2 行 2 列からなる行列 A が与えられるので、A R,Cを出力してください。

i = list(map(int, input().split()))# 0 横　1 縦

k = []
l = list(map(int, input().split()))
n = list(map(int, input().split()))

k.append(l)
k.append(n)

print(k[i[0]-1][i[1]-1])