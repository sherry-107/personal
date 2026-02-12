n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dat = [0] * 201
for i in segments:
    x1 = i[0] + 100
    x2 = i[1] + 100

    for j in range(x1, x2):
        dat[j] += 1

print(max(dat))

    
