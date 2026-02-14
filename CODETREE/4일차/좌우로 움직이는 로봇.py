n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.

a_arr = [0]
b_arr = [0]

for i in range(n):
    for j in range(t[i]):
        if d[i] == 'L':
            a_arr.append(a_arr[-1] - 1)
        else:
            a_arr.append(a_arr[-1] + 1)

for i in range(m):
    for j in range(t_b[i]):
        if d_b[i] == 'L':
            b_arr.append(b_arr[-1] - 1)
        else:
            b_arr.append(b_arr[-1] + 1)

cnt = 0

if len(a_arr)> len(b_arr):
    for i in range(1, len(a_arr)):
        if i >= len(b_arr):
            if b_arr[-1] == a_arr[i] and b_arr[-1] != a_arr[i-1]:
                cnt += 1
        else:
            if b_arr[i] == a_arr[i] and b_arr[i-1] != a_arr[i-1]:
                cnt += 1



else:
    for i in range(1, len(b_arr)):
        if i >= len(a_arr):
            if a_arr[-1] == b_arr[i] and a_arr[-1] != b_arr[i-1]:
                cnt += 1
        else:
            if a_arr[i] == b_arr[i] and a_arr[i-1] != b_arr[i-1]:
                cnt += 1
    
print(cnt)