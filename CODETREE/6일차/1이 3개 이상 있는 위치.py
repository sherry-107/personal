n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

delta1 = [1, -1, 0, 0]
delta2 = [0, 0, 1, -1]

cnt = 0

for i in range(n):
    for j in range(n):
        idx = 0

        for k in range(4):
            x1 = i + delta1[k]
            y1 = j + delta2[k]
            if 0 <= x1 < n and 0 <= y1 < n:
                if grid[x1][y1] == 1:
                    idx += 1

        if idx >= 3:
            cnt += 1

print(cnt)