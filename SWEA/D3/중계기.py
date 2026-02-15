t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n+1)]

    max_d = 0
    idx = 0

    for x in range(n+1):
        for y in range(n+1):
            if arr[x][y] == 2:
                
                for x1 in range(n+1):
                    for y1 in range(n+1):
                        if arr[x1][y1] == 1:
                            d = (x-x1)**2 + (y-y1)**2

                            max_d = max(max_d, d)

    for i in range(1, 15):
        if i**2 >= max_d:
            idx = i
            break

    print(f'#{tc} {idx}')