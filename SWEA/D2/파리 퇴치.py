t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for i in range(n)]

    max_v = 0

    for x in range(n-m+1):
        for y in range(n-m+1):
            v = 0
            for i in range(0, m):
                for j in range(0, m):
                    x1 = x + i
                    y1 = y + j

                    
                    v += arr[x1][y1]

            max_v = max(max_v, v)

    print(f'#{tc} {max_v}')
