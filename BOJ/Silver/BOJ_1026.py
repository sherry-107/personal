t = int(input())

a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

a_arr.sort()
S = 0

for i in range(t):
    max_v = max(b_arr)
    S += a_arr[i] * max_v
    idx = b_arr.index(max_v)
    b_arr[idx] = -1


print(S)