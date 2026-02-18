t = int(input())

for tc in range(1, t+1):
    n = int(input())

    arr = [list(map(int, input().split())) for i in range(n)]

    delta1 = [-1, 1, 0, 0]
    delta2 = [0, 0, -1, 1]
    max_v = 0

    for xx in range(n):
        for yy in range(n):
            x = xx
            y = yy
            cnt = 0
            move = True
            min_v = arr[x][y]

            while move == True:

                for i in range(4):
                    x1 = x + delta1[i]
                    y1 = y + delta2[i]

                    if 0 <= x1 < n and 0 <= y1 < n:
                        min_v = min(min_v, arr[x1][y1])

                if min_v == arr[x][y]:
                    move = False
                else:
                    for i in range(4):
                        x1 = x + delta1[i]
                        y1 = y + delta2[i]

                        if 0 <= x1 < n and 0 <= y1 < n:
                            if min_v == arr[x1][y1]:
                                x, y = x1, y1
                                break
                cnt += 1
            max_v = max(max_v, cnt)

    print(f'#{tc} {max_v}')