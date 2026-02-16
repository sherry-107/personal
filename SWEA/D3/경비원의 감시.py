t = int(input())

for tc in range(1, t+1):
    n = int(input())

    arr = [list(map(int, input().split())) for i in range(n)]
    delta1 = [1, -1, 0, 0]
    delta2 = [0, 0, 1, -1]

    v = 0

    for x in range(n):
        for y in range(n):

            if arr[x][y] == 2:
                for i in range(4):
                    j = 0
                    while j <= n-1:
                        j += 1
                
                        x1 = x + delta1[i] * j
                        y1 = y + delta2[i] * j

                        if 0 <= x1 < n and 0 <= y1 < n:
                            if arr[x1][y1] == 1:
                                break
                            else:
                                arr[x1][y1] = 9

    for x in range(n):
        for y in range(n):
            if arr[x][y] == 0:
                v += 1

    print(f'#{tc} {v}')
