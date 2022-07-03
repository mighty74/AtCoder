N = int(input())

n = N // 60
k = N % 60
d = n + 21
s = f'{k:02}'
print(d, end='')
print(":", end='')
print(s)