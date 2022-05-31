i = list(map(int, input().split()))
m = list(map(int, input().split()))
num = []

def count3(list, max):
    for d in range(len(list)-2):
        for k in range(len(list)-2-d):
            for l in range(len(list)-2-d-k):
                if list[d]+list[d+k+1]+list[d+k+l+2] <= max:
                    num.append(list[d]+list[d+k+1]+list[d+k+l+2])

def count2(list, max):
    for d in range(len(list)-1):
        for k in range(len(list)-1-d):
            if list[d]+list[d+k+1] <= max:
                num.append(list[d]+list[d+k+1])

def count1(list, max):
    for d in list:
        if d <= max:
            num.append(d)


if i[0] >= 3:
    count1(m, i[1])
    count2(m, i[1])
    count3(m, i[1])
if i[0] == 2:
    count1(m, i[1])
    count2(m, i[1])
if i[0] == 1:
    count1(m, i[1])

Num = set(num)
print(len(Num))
print(Num)

