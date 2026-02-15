t = int(input())

for tc in range(1, t+1):
    n = int(input())
    dat = [0]*5001

    for i in range(n):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            dat[j] += 1

    p = int(input())

    print(f'#{tc} ', end = '')

    for i in range(p):
        c = int(input())

        print(dat[c], end = ' ')