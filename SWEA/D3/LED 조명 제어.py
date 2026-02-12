t = int(input())

for tc in range(1, t+1):
    n = int(input())
    find_arr = list(map(int, input().split()))
    find_arr.insert(0, 0)
    prob_arr = [0]*(n+1)
    cnt = 0

    for i in range(0, n+1):
        if find_arr[i] != prob_arr[i]:
            cnt += 1

            for j in range(i, n+1, i):
                if prob_arr[j] == 0:
                    prob_arr[j] = 1
                else:
                    prob_arr[j] = 0

    print(f'#{tc} {cnt}')