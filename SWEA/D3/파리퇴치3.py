t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(n)]

    delta1 = [1, -1, 0, 0, 1, -1, 1, -1]
    delta2 = [0, 0, 1, -1, 1, 1, -1, -1]

    max_v = 0 

    for x in range(n):
        for y in range(n):
            v1 = arr[x][y]
            v2 = arr[x][y]

            for i in range(4):
                for j in range(1, m):
                    x1 = x + delta1[i] * j
                    y1 = y + delta2[i] * j

                    if 0<= x1 < n and 0<= y1< n:
                        v1 += arr[x1][y1]

            for i in range(4, 8):
                for j in range(1, m):
                    x1 = x + delta1[i] * j
                    y1 = y + delta2[i] * j

                    if 0<= x1 <n and 0<= y1 < n:
                        v2 += arr[x1][y1]

            max_v = max(max_v, v1, v2)

    print(f'#{tc}', max_v)
