t = int(input())

for tc in range(1, t+1):
    n, m, k = map(int, input().split())

    arr = [list(map(int, input().split())) for i in range(n)]
    turn = []
    min_v = float('inf')

    for i in range(k):
        r, c, s = map(int, input().split())
        turn.append((r, c, s))

    order = []

    def calc(arr):
        global min_v

        for i in arr:
            min_v = min(min_v, sum(i))


    def func():
        if len(order) == len(turn):
            new_arr = [row[:] for row in arr]
            for r, c, s in order:
                start_x, start_y = r-s-1, c-s-1
                end_x, end_y = r+s-1, c+s-1

                while start_x < end_x and start_y < end_y:
                    v = new_arr[start_x][start_y]

                    for i in range(start_x, end_x):
                        new_arr[i][start_y] = new_arr[i+1][start_y]
                    
                    for i in range(start_y, end_y):
                        new_arr[end_x][i] = new_arr[end_x][i+1]
                    
                    for i in range(end_x, start_x, -1):
                        new_arr[i][end_y] = new_arr[i-1][end_y]
                    
                    for i in range(end_y, start_y, -1):
                        new_arr[start_x][i] = new_arr[start_x][i-1]
                    
                    new_arr[start_x][start_y+1] = v

                    start_x += 1
                    start_y += 1
                    end_x -= 1
                    end_y -= 1

            calc(new_arr)
            return

        for i in range(len(turn)):
            if turn[i] not in order:
                order.append(turn[i])
                func()
                order.pop()

    func()
    print(f'#{tc} {min_v}')