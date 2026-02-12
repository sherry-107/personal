t = int(input())

for tc in range(1, t+1):
    n = int(input())

    arr = [list(map(int, input().split())) for i in range(n)]
    width_arr = []
    max_v = 0
    cnt = 0

    for i in range(n):
        for j in range(n):
            for k in range(i, n):
                for r in range(j, n):
                    if arr[i][j] == arr[k][r]:
                        width = (k-i+1)*(r-j+1)
                        width_arr.append(width)
                        max_v = max(max_v, width)

    for i in width_arr:
        if i == max_v:
            cnt += 1

    print(f'#{tc} {cnt}')