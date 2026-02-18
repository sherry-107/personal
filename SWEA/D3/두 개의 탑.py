t = int(input())

for tc in range(1, t+1):
    n, m1, m2 = map(int, input().split())

    arr = list(map(int, input().split()))
    arr.sort()

    top1 = []
    top2 = []

    top1_v = 0
    top2_v = 0

    for i in range(1, min(m1, m2) + 1):
        a = arr.pop()
        top1.append(a)
        b = arr.pop()
        top2.append(b)
        
    if m1 > m2:
        top1 += arr
    else:
        top2 += arr

    top1.sort(reverse=True)
    top2.sort(reverse=True)

    for i in range(1, len(top1)+1):
        top1_v += i * top1[i-1]
    for i in range(1, len(top2) + 1):
        top2_v += i * top2[i-1]

    print(f'#{tc} {top1_v + top2_v}')