t = int(input())

for tc in range(1, t+1):
    n = int(input())
    sample = list(map(int, input()))
    m = int(input())
    problem = list(map(int, input()))

    idx = 0

    for i in sample:
        if i == problem[idx]:
            idx += 1
        if idx == m:
            break

    if idx == m:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)