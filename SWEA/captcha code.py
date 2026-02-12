t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())

    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))

    index = 0
    for num in sample:
        if index < k and num == passcode[index]:
            index += 1

    if index == k:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)