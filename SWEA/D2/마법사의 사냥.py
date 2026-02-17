n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]
k = int(input())

max_v = 0
delta1 = [1, -1, 1, -1]
delta2 = [1, 1, -1, -1]

for x in range(n):
    for y in range(n):
        v = 0

        for i in range(4):
            for j in range(1, k+1):
                x1 = x + delta1[i] * j
                y1 = y + delta2[i] * j

                if 0 <= x1 < n and 0 <= y1 < n:
                    v += arr[x1][y1]


        max_v = max(v, max_v)

print(max_v)