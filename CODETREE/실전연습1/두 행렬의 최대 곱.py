n, m = map(int, input().split())

n_arr = [list(map(int, input().split())) for i in range(n)]
m_arr = [list(map(int, input().split())) for j in range(m)]

max_v = -100000

for i in range(0, m-n+1):
    for j in range(0, m-n+1):
        v = 0
        for k in range(0, n):
            for r in range(0, n):
                v += n_arr[k][r] * m_arr[i+k][j+r]

        max_v = max(max_v, v)

print(max_v)

