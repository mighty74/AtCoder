import math

i = list(map(int, input().split()))

ra = math.atan2(i[1], i[0])
anX = math.cos(ra)
anY = math.sin(ra)
print('{:.12f}'.format(anX) + ' ' + '{:.12f}'.format(anY))