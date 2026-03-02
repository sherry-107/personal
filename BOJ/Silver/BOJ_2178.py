n, m = map(int, input().split())

arr = [list(map(int, input())) for i in range(n)]

delta1 = [1, -1, 0, 0]
delta2 = [0, 0, 1, -1]

visited = [[False] * m for i in range(n)]
visited[0][0] = True

que = []
que.append((0, 0))

while que:
    v = que.pop(0)
    x = v[0]
    y = v[1]

    for i in range(4):
        x1 = x + delta1[i]
        y1 = y + delta2[i]

        if 0 <= x1 < n and 0 <= y1 < m:
            if arr[x1][y1] != 0 and not visited[x1][y1]:
                visited[x1][y1] = True
                que.append((x1, y1))
                arr[x1][y1] = arr[x][y] + 1

print(arr[-1][-1])