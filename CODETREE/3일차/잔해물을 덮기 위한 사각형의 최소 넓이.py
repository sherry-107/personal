x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

dat = [[0] * 2001 for i in range(2001)]

for x in range(x1[0] + 1000, x2[0] + 1000):
    for y in range(y1[0] + 1000, y2[0] + 1000):
        dat[x][y] = 1

for x in range(x1[1]+1000, x2[1]+1000):
    for y in range(y1[1] + 1000, y2[1] + 1000):
        if dat[x][y] == 1:
            dat[x][y] = 0

max_x, max_y, min_x, min_y = 3000, 3000, -3000, -3000
found = 0

for i in range(x1[0]+1000, x2[0] + 1000):
    for j in range(y1[0] + 1000, y2[0] + 1000):
        if dat[i][j] == 1:
            found = 1
            if max_x < i:
                max_x = i
            if max_y < j:
                max_y = j
            if min_x > i:
                min_x = i
            if min_y > j:
                min_y = j

if found == 0:
    print(0)
else:
    print((max_x - min_x + 1) * (max_y - min_y + 1))
            
