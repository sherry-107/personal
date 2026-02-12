n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dat = [0]*101

for i in segments:
    x1 = i[0]
    x2 = i[1]

    for j in range(x1, x2+1):
        dat[j] += 1

print(max(dat))