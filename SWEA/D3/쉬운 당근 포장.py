t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))

    dict = {}
    min_v = 10000000

    for i in arr:
        dict[i] = 0

    if len(dict.keys()) <= 2:
        min_v = -1

    else:
        for i in arr:
            dict[i] += 1

        carrot = list(dict.keys())

        for i in range(len(carrot)-2):
            for j in range(i+1, len(carrot)-1):

                s = 0
                m = 0
                l = 0

                for k in range(0, i+1):
                    s += dict[carrot[k]]
                for k in range(i+1, j+1):
                    m += dict[carrot[k]]

                l = n - s - m

                min_v = min(min_v, max(s, m, l) - min(s, m, l))
    print(f'#{tc} {min_v}')