n, m = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(n)]

chicken = []
house = []

result = float('inf')

for x in range(n):
    for y in range(n):
        if arr[x][y] == 2:
            chicken.append((x, y))
        elif arr[x][y] == 1:
            house.append((x, y))

choose = []

def func(level, start):
    global result
    if level == m:
        v = 0
        for x, y in house:
            min_v = float('inf')
            for i, j in choose:
                min_v = min(min_v, abs(x-i) + abs(y-j))
            v += min_v
        result = min(result, v)
        return

    for i in range(start, len(chicken)):
        choose.append(chicken[i])
        func(level+1, i+1)
        choose.pop()

func(0, 0)

print(result)