t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())

    arr = [list(map(int, input().split())) for i in range(n)]
    cnt = 0

    for x in range(0, n-k+1):
        for y in range(0, n):
            if arr[x][y] == 1:
                idx = True
                for i in range(1, k):
                    x1 = x + i
                    if arr[x1][y] != 1:
                        idx = False

                if idx:
                    if 0 <= x-1 < n:
                        if arr[x - 1][y] == 1:
                            idx = False
                    if 0 <= x + k < n:
                        if arr[x + k][y] == 1:
                            idx = False
                if idx:
                    cnt += 1
                    
    for x in range(0, n):
        for y in range(0, n-k+1):
            if arr[x][y] == 1:
                idx = True

                for i in range(1, k):
                    y1 = y + i
                    if arr[x][y1] != 1:
                        idx = False
                if idx:
                    if 0 <= y - 1 < n:
                        if arr[x][y-1] == 1:
                            idx = False
                    if 0 <= y + k < n:
                        if arr[x][y + k] == 1:
                            idx = False
                if idx:
                    cnt += 1

    print(f'#{tc} {cnt}')