t = int(input())

for tc in range(1, t+1):
    n = int(input())
    ans_arr = list(map(int, input().split()))
    pro_arr = [0]*n

    cnt = 0
    for i in range(n):
        if ans_arr[i] != pro_arr[i]:
            cnt += 1
            for j in range(i, n, i+1):
                if pro_arr[j] == 0:
                    pro_arr[j] = 1
                else:
                    pro_arr[j] = 0

    print(f'#{tc} {cnt}')