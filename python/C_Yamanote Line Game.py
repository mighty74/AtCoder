from bisect import bisect_left


n = int(input())
flag = True
List = [1]

for k in range(2*n+1):
    if k != 0:
        List.append(List[k-1]+1)

while flag:
    if len(List) != 0:
        p = List.pop(0)
        print(p, flush=True)
    d = int(input())
    if len(List) != 0:
        k = bisect_left(List, d)
        p = List.pop(k)
    else:
        #p = 0
        flag = False
        #print(p, flush=True)
    #print("残りの数"+str(len(List)))

