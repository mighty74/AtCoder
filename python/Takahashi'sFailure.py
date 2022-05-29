
i = list(map(int, input().split()))
l = list(map(int, input().split()))
k = list(map(int, input().split()))

answer = "No"
max = 0;
for what in l:
    if max < what:
        max = what

for D in k:
    if l[D-1] == max:
        answer = "Yes"

print(answer)