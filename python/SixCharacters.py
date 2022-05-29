i = str(input())
k = 0;
if len(i)==1:
    k = 5
elif len(i)==2:
    k = 2
else:
    k = 1

t = i

for num in range(k):
    t += i

print(t)