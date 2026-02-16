t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))

    dat = [0] * n
    dat[0] = 1

    idx = 0
    cnt = 0

    while idx < n-1:
        if dat[idx] == 1:
            idx += 1
        else:
            dat[idx] = 1
            idx = arr[idx] - 1
        cnt += 1

    print(f'#{tc} {cnt}')