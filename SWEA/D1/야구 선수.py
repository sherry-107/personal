t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))
    max_cnt = 0
    arr.sort()

    for i in range(0, n):
        cnt = 1
        for j in range(i+1, n):
            if arr[j] - arr[i] <= k:
                cnt += 1

        max_cnt = max(cnt, max_cnt)

    print(f'#{tc} {max_cnt}')