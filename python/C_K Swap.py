i = list(map(int, input().split()))
l = list(map(int, input().split()))
k = l.copy()
k.sort()
flag = "No"
flag1 = False
flag0 = False
if l == k or i[1] == 1:
    flag = "Yes"

if flag == "No":
    for d in range(i[0]-i[1]):
        for n in range((int)((i[0]-d-1)/i[1])+1):
            if k[d] == l[d+n*i[1]]:
                temp = l[d+n*i[1]]
                l[d+n*i[1]] = l[d]
                l[d] = temp
                break
            elif n == (int)((i[0]-d)/i[1]):
                flag0 = True
                break
        if flag0:
            break
        if l == k:
            flag = "Yes"
            break

# if l == k:
#     flag = "Yes"


print(flag)



# if flag == "No":
#     for n in range(i[0]-i[1]):
#         for j in range(i[0]-i[1]-n):
#             if l[n+j] > l[n+j+i[1]]:
#                 temp = l[n+j]
#                 l[n+j] = l[n+j+i[1]]
#                 l[n+j+i[1]] = temp
#             if l == k:
#                 flag1 = True
#                 break
#         if flag1:
#             break

# if l == k:
#     flag = "Yes"


# print(flag)
