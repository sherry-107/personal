t = int(input())

for tc in range(1, t+1):
    paper = [5] * 6
    arr = [list(map(int, input().split())) for i in range(10)]
    min_v = float('inf')

    def stitch(x, y, d, num):
        for i in range(d+1):
            for j in range(d+1):
                arr[x+i][y+j] = num

    def func(xy, paper, count):
        global min_v
        if xy == 100:
            min_v = min(min_v, count)
            return
        
        if count >= min_v:
            return
        
        for cnt in paper:
            if cnt < 0:
                return
            
        x, y = xy//10, xy%10

        if arr[x][y] == 0:
            func(xy+1, paper, count)
            return
        
        if arr[x][y] == 1:
            for d in range(4, -1, -1):
                
                idx = True
                if x + d < 10 and y+d < 10:
                    for i in range(d+1):
                        for j in range(d+1):
                            if arr[x+i][y+j] == 0:
                                idx = False
                else:
                    idx = False

                if idx:
                    stitch(x, y, d, 0)
                    paper[d] -= 1
                    func(xy+1, paper, count+1)
                    stitch(x, y, d, 1)
                    paper[d] += 1

    func(0, paper, 0)
            
    if min_v == float('inf'):
        print(f'#{tc}', -1)
    else:
        print(f'#{tc} {min_v}')

