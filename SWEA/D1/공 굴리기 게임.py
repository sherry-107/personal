t = int(input())

for tc in range(1, t+1):
    n = int(input())

    arr = [list(map(int, input().split())) for i in range(n)]
    delta1 = [-1, 1, 0, 0]
    delta2 = [0, 0, -1, 1]

    max_cnt = 0

    for xx in range(n):
        for yy in range(n):
            move = True
            cnt = 1
            x, y = xx, yy

            while move == True:
                min_v = arr[x][y]
                
                for i in range(4):
                    x1 = x + delta1[i]
                    y1 = y + delta2[i]

                    if 0 <= x1 < n and 0 <= y1 < n:
                        min_v = min(min_v, arr[x1][y1])

                if min_v == arr[x][y]:
                    move = False
                else:
                    cnt += 1
                    for i in range(4):
                        x1 = x + delta1[i]
                        y1 = y + delta2[i]

                        if 0 <= x1 < n and 0 <= y1 < n and arr[x1][y1] == min_v:
                            x, y = x1, y1
                            break
                                

                       
            max_cnt = max(max_cnt, cnt)

    print(f'#{tc} {max_cnt}')
