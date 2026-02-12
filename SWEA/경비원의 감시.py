t = int(input())

for tc in range(1, t+1):
    n = int(input())

    arr = [list(map(int, input().split())) for i in range(n)]

    delta1 = [1, -1, 0, 0]
    delta2 = [0, 0, 1, -1]

    for x in range(n):
        for y in range(n):
            if arr[x][y] == 2:
                
                i = 0
                while i < 4:
                    for j in range(1, n):
                        x1 = x + delta1[i] * j
                        y1 = y + delta2[i] * j

                        if 0<=x1<n and 0<=y1<n:
                            if arr[x1][y1] == 1:
                                break
                            if arr[x1][y1] == 0:
                                arr[x1][y1] = 5
                    i += 1

    sum_v = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                sum_v += 1

    print(f'#{tc}', sum_v)