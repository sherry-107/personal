n = int(input())

arr = [list(map(int, input())) for i in range(n)]
delta1 = [1, -1, 0, 0]
delta2 = [0, 0, 1, -1]
visited = [[False]*n for i in range(n)]

result = []

def func(x, y):
    v = 1
    for i in range(4):
        x1 = x + delta1[i]
        y1 = y + delta2[i]

        if 0 <= x1 < n and 0 <= y1 < n:
            if arr[x1][y1] == 1 and not visited[x1][y1]:
                visited[x1][y1] = True
                v += func(x1, y1)
    return v

for x in range(n):
    for y in range(n):
        if arr[x][y] == 1 and not visited[x][y]:
            visited[x][y] = True
            result.append(func(x, y))

print(len(result))

result.sort()

for i in result:
    print(i)