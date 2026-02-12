t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(n)]
    cnt = 0


    for x in range(n):
        for y in range(0, n-k+1):
            idx = 1
            for i in range(0, k):
                if arr[x][y+i] != 1:
                    idx = 0

            if idx == 1:
                if y + k <= n - 1:
                    if arr[x][y+k] == 1:
                        idx = 0
                if y - 1 >= 0:
                    if arr[x][y-1] == 1:
                        idx = 0
            if idx == 1:
                cnt += 1

    arr2 = []

    for i in range(n):
        a = []
        for j in range(n):
            a.append(arr[j][i])
        arr2.append(a)

    for x in range(n):
        for y in range(0, n - k + 1):
            idx = 1
            for i in range(0, k):
                if arr2[x][y + i] != 1:
                    idx = 0

            if idx == 1:
                if y + k <= n - 1:
                    if arr2[x][y + k] == 1:
                        idx = 0
                if y - 1 >= 0:
                    if arr2[x][y - 1] == 1:
                        idx = 0
            if idx == 1:
                cnt += 1

    print(f'#{tc} {cnt}')