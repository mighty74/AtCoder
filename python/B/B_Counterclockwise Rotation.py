import math

a, b, d = map(int, input().split())

R = math.sqrt((a ** 2) + (b ** 2))
r = 0
if R != 0:
    k = math.degrees(math.asin(abs(b) / R))
    if a >= 0 and b >= 0:
        r = k + d
    if a <= 0 and b >= 0:
        r = 180 - k + d
    if a <= 0 and b <= 0:
        r = 180 + k + d
    if a >= 0 and b <= 0:
        r = 360 - k + d
print(R * math.cos(math.radians(r)), end = ' ')
print(R * math.sin(math.radians(r)))