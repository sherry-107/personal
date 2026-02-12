n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.

dat = [0] * 2001
a = 1000

for i in range(n):
    for j in range(x[i]):
        if dir[i] == 'R':
            a += 1
            dat[a] += 1
        else:
            dat[a] += 1
            a -= 1

cnt = 0
for i in dat:
    if i >= 2:
        cnt += 1

print(cnt)