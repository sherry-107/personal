import sys
sys.setrecursionlimit(10000)

t = int(input())

for tc in range(1, t+1):
    n, m, k = map(int, input().split())

    arr = [[0]*m for i in range(n)]
    delta1 = [1, -1, 0, 0]
    delta2 = [0, 0, 1, -1]

    num = 0

    for i in range(k):
        x, y = map(int, input().split())

        arr[x][y] = 1

    def delta_func(arr, x, y):
        arr[x][y] = 0

        for i in range(4):

            x1 = x + delta1[i]
            y1 = y + delta2[i]

            if 0 <= x1 < n and 0 <= y1 < m and arr[x1][y1] == 1:
                delta_func(arr, x1, y1)

    for x in range(n):
        for y in range(m):
            if arr[x][y] == 1:
                num += 1
                delta_func(arr, x, y)
    print(num)






