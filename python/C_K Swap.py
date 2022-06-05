i = list(map(int, input().split()))
l = list(map(int, input().split()))
k = l.copy()
k.sort()
flag = "No"
flag1 = True
if l == k:
    flag = "Yes"

if flag == "No":
    for n in range(i[0]-i[1]):
        for j in range(i[0]-i[1]-n):
            if l[n+j] > l[n+j+i[1]]:
                temp = l[n+j]
                l[n+j] = l[n+j+i[1]]
                l[n+j+i[1]] = temp

if l == k:
    flag = "Yes"


print(flag)
