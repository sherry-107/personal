t = int(input())

for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for i in range(9)]

    idx = 1

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            num_arr = []
            for i in range(3):
                for j in range(3):
                    x1 = x + i
                    y1 = y + j

                    if arr[x1][y1] in num_arr:
                        idx = 0
                        break
                    else:
                        num_arr.append(arr[x1][y1])

    if idx == 1:
        for x in range(9):
            num_arr = []
            for i in range(9):
                if arr[x][i] in num_arr:
                    idx = 0
                    break
                else:
                    num_arr.append(arr[x][i])
    if idx == 1:
        for y in range(9):
            num_arr = []
            for j in range(9):
                if arr[j][y] in num_arr:
                    idx = 0
                    break
                else:
                    num_arr.append(arr[j][y])

    print(f'#{tc} {idx}')
