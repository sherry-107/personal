x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.

dat = [[0]*2001 for i in range(2001)]

for i in range(x1[0] + 1000, x2[0] + 1000):
    for j in range(y1[0] + 1000, y2[0] + 1000):
        dat[i][j] = 1

for i in range(x1[1] + 1000, x2[1] + 1000):
    for j in range(y1[1] + 1000, y2[1] + 1000):
        dat[i][j] = 0

max_x = 0
min_x = 2000
max_y = 0
min_y = 2000

idx = 1

for x in range(x1[0] + 1000, x2[0] + 1000):
    for y in range(y1[0] + 1000, y2[0] + 1000):
        if dat[x][y] == 1:
            idx = 0
            max_x = max(x, max_x)
            min_x = min(x, min_x)
            max_y = max(max_y, y)
            min_y = min(min_y, y)

if idx == 1:
    width = 0
else:
    width = (max_x - min_x + 1) * (max_y - min_y + 1)
print(width)

