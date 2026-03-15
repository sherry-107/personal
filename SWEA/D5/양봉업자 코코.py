t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for i in range(n)]

    odd_delta1 = [1, -1, 0, 0, 1, 1]
    odd_delta2 = [0, 0, 1, -1, 1, -1]
    even_delta1 = [1, -1, 0, 0, -1, -1]
    even_delta2 = [0, 0, 1, -1, 1, -1]

    visited = [[False] * m for i in range(n)]

    max_v = 0

    def honey(level, v, x, y):
        global max_v
        if level == 3:
            max_v = max(v, max_v)
            return

        result = v
        for i in range(6):
            if y % 2 == 0:
                x1 = x + even_delta1[i]
                y1 = y + even_delta2[i]

            else:
                x1 = x + odd_delta1[i]
                y1 = y + odd_delta2[i]

            if 0 <= x1 < n and 0 <= y1 < m and not visited[x1][y1]:
                visited[x1][y1] = True
                honey(level+1, v+arr[x1][y1], x1, y1)

                if level == 1:
                    honey(level+1, v+arr[x1][y1], x, y)
                visited[x1][y1] = False

    for x in range(n):
        for y in range(m):
            visited[x][y] = True
            honey(0, arr[x][y], x, y)
            visited[x][y] = False

    print(f'#{tc} {max_v}')