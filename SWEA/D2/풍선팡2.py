t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(n)]

    delta1 = [1, -1, 0, 0]
    delta2 = [0, 0, 1, -1]

    max_v = 0

    for x in range(n):
        for y in range(m):
            v = arr[x][y]

            for i in range(4):
                x1 = x + delta1[i]
                y1 = y + delta2[i]

                if 0<=x1<n and 0<=y1<m:
                    v += arr[x1][y1]

            max_v = max(max_v, v)

    print(f'#{tc}', max_v)