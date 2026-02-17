t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    
    carrot = {}

    min_v = 10000000

    for i in arr:
        carrot[i] = 0

    if len(carrot.keys()) <= 2:
        min_v = -1

    else:
        for i in arr:
            carrot[i] += 1

        sorted_carrot = sorted(carrot.keys())

        for i in range(len(sorted_carrot) - 2):
            for j in range(i+1, len(sorted_carrot) - 1):

                s_cnt = 0
                m_cnt = 0
                l_cnt = 0

                for k in range(0, i+1):
                    s_cnt += carrot[sorted_carrot[k]]
                for k in range(i+1, j+1):
                    m_cnt += carrot[sorted_carrot[k]]

                l_cnt = len(arr) - s_cnt - m_cnt

                min_v = min(min_v, max(s_cnt, m_cnt, l_cnt) - min(s_cnt, m_cnt, l_cnt))

    print(f'#{tc} {min_v}')
