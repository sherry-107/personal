n, m = map(int, input().split())
k = int(input())

arr = [list(map(str, input())) for i in range(n)]

delta1 = [1, -1, 0, 0]
delta2 = [0, 0, 1, -1]

for x in range(n):
    for y in range(m):
        if arr[x][y] == '@':
            arr[x][y] = '%'
            
            i = 0
            while i < 4:
                for j in range(1 , k+1):
                    x1 = x + delta1[i] * j
                    y1 = y + delta2[i] * j

                    if 0<= x1 < n and 0<= y1 < m:
                        if arr[x1][y1] == '#':
                            break
                        if arr[x1][y1] == '_':
                            arr[x1][y1] = '%'
                            
                i+=1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = '')
    print()