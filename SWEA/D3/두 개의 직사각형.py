t = int(input())

for tc in range(1, t+1):
    x1, x2, y1, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
    x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
    x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

    dat = [[0] * 1002 for i in range(1002)]

    for i in range(x1[0], x2[0]+1):
        for j in range(y1[0], y2[0]+1):
            dat[i][j] += 1

    for i in range(x1[1], x2[1]+1):
        for j in range(y1[1], y2[1]+1):
            dat[i][j] += 2

    cnt = 0
    cnt2 = 0

    for i in range(x1[0], x2[0]+1):
        for j in range(y1[0], y2[0]+1):
            if dat[i][j] == 3:
                cnt += 1

    if cnt == 0:
        idx = 4
    elif cnt == 1:
        idx = 3
    else:
        for i in range(x1[0]+1, x2[0]):
            for j in range(y1[0]+1, y2[0]):
                if dat[i][j] == 3:
                    cnt2 += 1
        if cnt2 == 0:
            idx = 2
        else:
            idx = 1

    print(f'#{tc} {idx}')
