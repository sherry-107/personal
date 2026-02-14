n, k = map(int, input().split())

arr = list(map(int, input().split()))
cnt = 0

for i in range(n):
    idx = 1
    for j in range(i-k, i+k+1):
        if 0<= j <n:
            if arr[i] < arr[j]:
                idx = 0

    cnt += idx

print(cnt)