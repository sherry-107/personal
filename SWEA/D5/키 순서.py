from collections import deque

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    m = int(input())
    
    tall = [[] for i in range(n+1)]
    short = [[] for i in range(n+1)]

    cnt = 0

    for i in range(m):
        a, b = map(int, input().split())

        tall[b].append(a)
        short[a].append(b)

    for student in range(1, n+1):
        tall_que = deque([])
        short_que = deque([])

        que = []

        tall_que.append(student)
        short_que.append(student)

        while tall_que:
            v = tall_que.popleft()

            if len(tall[v]) != 0:
                for i in tall[v]:
                    if i not in que:
                        que.append(i)
                        tall_que.append(i)
        
        while short_que:
            v = short_que.popleft()

            if len(short[v]) != 0:
                for i in short[v]:
                    if i not in que:
                        que.append(i)
                        short_que.append(i)

        if len(que) == n-1:
            cnt += 1
    
    print(f'#{tc} {cnt}')
