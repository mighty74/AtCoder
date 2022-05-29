# 整数 a,b,c が与えられます。
# b がこれらの整数の中央値であるかどうか判定してください。

i = list(map(int, input().split()))
k = "No"

if i[0] <= i[1] and i[1] <= i[2]:
    k = "Yes"
if i[0] >= i[1] and i[1] >= i[2]:
    k = "Yes"
print(k)