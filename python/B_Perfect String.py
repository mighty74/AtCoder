moji = input()
i = list(moji)
komoji = moji.islower()
omoji = moji.isupper()
an = 'Yes'
flag = False
if not komoji and not omoji:
    for k in range(len(i)):
        for d in range(len(i)-k-1):
            #print(i[k])
            if i[k] == i[k+d+1]:
                flag = True
                an = 'No'
                break
        if flag:
            break
else:
    an = 'No'
print(an)