t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    i = 0

    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))
    
    for txt in sample:
        if txt == passcode[i]:
            i += 1
        if i == k:
            break

    if i == k:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)