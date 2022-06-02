i = list(map(int, input().split()))

for y in range(i[0]):
    for k in range(i[1]):
        for x in range(i[0]):
            for n in range(i[2]):
                if x%2 == 1 and y%2 == 1:
                    print('.' ,end='')
                if x%2 == 0 and y%2 == 0:
                    print('.' ,end='')
                if x%2 == 1 and y%2 == 0:
                    print('#' ,end='')
                if x%2 == 0 and y%2 == 1:
                    print('#' ,end='')
        print()
