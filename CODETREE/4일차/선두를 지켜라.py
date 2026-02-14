n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.

a_arr = [0]
b_arr = [0]

for i in range(n):
    for j in range(t[i]):
        a_arr.append(a_arr[-1] + v[i])

for i in range(m):
    for j in range(t2[i]):
        b_arr.append(b_arr[-1] + v2[i])

cnt = 0
idx = -1

for i in range(1, len(a_arr)):
    if a_arr[i] > b_arr[i] and idx != 0:
        idx = 0
        cnt += 1
    elif a_arr[i] < b_arr[i] and idx != 1:
        idx = 1
        cnt += 1

print(cnt - 1)
