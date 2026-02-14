n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

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
    for j in range(t2[i]):
        if d2[i] == 'L':
            b_arr.append(b_arr[-1] - 1)
        else:
            b_arr.append(b_arr[-1] + 1)

index = -1
for i in range(1, len(a_arr)):
    if a_arr[i] == b_arr[i]:
        index = i
        break

print(index)