n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.

dat = [[0]*201 for i in range(201)]
offset = 100
cnt = 0

for i in range(n):
    for x1 in range(x[i] + offset, x[i] + 8 + offset):
        for y1 in range(y[i] + offset, y[i] + 8 + offset):
            if dat[x1][y1] == 0:
                cnt += 1
                dat[x1][y1] = 1

print(cnt)