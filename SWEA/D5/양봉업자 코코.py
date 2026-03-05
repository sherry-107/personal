t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for i in range(n)]

    even_delta1 = [1, -1, 0, 0, -1, -1]
    even_delta2 = [0, 0, 1, -1, 1, -1]

    odd_delta1 = [1, -1, 0, 0, 1, 1]
    odd_delta2 = [0, 0, 1, -1, 1, -1]

    def honey(x, y, level, cost, visited):
        if level == 3:
            return cost
        
        res = cost
        for i in range(6):
            if y%2 == 0:
                x1 = x + even_delta1[i]
                y1 = y + even_delta2[i]
            else:
                x1 = x + odd_delta1[i]
                y1 = y + odd_delta2[i]

            if 0 <= x1 < n and 0 <= y1 < m:
                if not visited[x1][y1]:
                    visited[x1][y1] = True
                    res = max(res, honey(x1, y1, level+1, cost + arr[x1][y1], visited))
                    
                    if level == 1:
                        res = max(res, honey(x, y, level+1, cost + arr[x1][y1], visited))
                    
                    visited[x1][y1] = False
        return res
    
    max_v = 0

    for x in range(n):
        for y in range(m):
            visited = [[False] * m for i in range(n)]
            visited[x][y] = True
            max_v = max(max_v, honey(x, y, 0, arr[x][y], visited))
    
    print(f'#{tc} {max_v}')