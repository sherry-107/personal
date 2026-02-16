t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())

    ans_arr = list(map(int, input().split()))
    pro_arr = [list(map(int, input().split())) for i in range(n)]

    score_arr = []

    for pro in pro_arr:
        v = 0
        for i in range(m):
            v1 = 0
            if pro[i] == ans_arr[i]:
                for j in range(0, i):
                    if pro[j] == ans_arr[j]:
                        v1 += 1
                    else:
                        v1 = 0

                v += v1+1

        score_arr.append(v)

    print(f'#{tc}', max(score_arr) - min(score_arr))
