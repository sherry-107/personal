t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    idx = 0

    while True:
        jump = False
    
        for i in range(k, 0, -1):
            if idx + i < len(arr) and arr[idx + i] == 1:
                idx = idx + i
                jump = True
                break

        if not jump:
            break

    if idx + k >= len(arr):
        idx = len(arr) - 1
    else:
        idx += k
    print(f'#{tc} {idx+1}')

            
