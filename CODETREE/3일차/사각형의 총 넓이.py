n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.

dat = [[0]*250 for i in range(250)]
cnt = 0

for i in range(n):
    for x in range(x1[i] + 100, x2[i] + 100):
        for y in range(y1[i] + 100, y2[i] + 100):
            if dat[x][y] == 0:
                cnt += 1
            dat[x][y] = 1

print(cnt)