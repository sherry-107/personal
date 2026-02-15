n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

arr = [[0] * (n+1) for i in range(n+1)]

delta1 = [1, -1, 0, 0]
delta2 = [0, 0, 1, -1]

for i in range(m):
    x = points[i][0]
    y = points[i][1]

    arr[x][y] = 1
    cnt = 0

    for j in range(4):
        x1 = x + delta1[j]
        y1 = y + delta2[j]

        if 1 <= x1 < n+1 and 1 <= y1 < n+1:
            if arr[x1][y1] == 1:
                cnt += 1

    if cnt == 3:
        idx = 1
    else:
        idx = 0
    print(idx)