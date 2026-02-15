n = int(input())
arr = list(map(int, input().split()))

dp = [float('inf')] * n

dp[0] = 0

for i in range(n):
    if arr[i] != 0:
        if i+1 < n and arr[i+1] == 1:
            dp[i+1] = min(dp[i+1], dp[i]+1)
        if i+3 < n and arr[i+3] == 1:
            dp[i+3] = min(dp[i+3], dp[i]+1)

if dp[n-1] == float('inf'):
    print(-1)
else:
    print(dp[n-1])