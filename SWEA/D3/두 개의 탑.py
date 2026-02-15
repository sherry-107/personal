t = int(input())

for tc in range(1, t+1):
    n, m1, m2 = map(int, input().split())

    arr = list(map(int, input().split()))
    arr.sort()

    cost = 0

    for i in range(1, max(m1, m2)+1):
        if i <= m1:
            cost += i * arr.pop()

        if i <= m2:
            cost += i * arr.pop()

    print(f'#{tc} {cost}')