n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.

k -= 1
cnt = 0

if k < n:
    x = 0
    y = k
    dir = 'D'
elif k < 2*n:
    y = n-1
    x = k%n
    dir = 'L'
elif k < 3*n:
    x = n-1
    y = n-(k%n)-1
    dir = 'U'
else:
    x = n-(k%n)-1
    y = 0
    dir = 'R'

while 0 <= x <= n-1 and 0 <= y <= n-1:
    if grid[x][y] == '/':
        if dir == 'D':
            dir = 'L'
            y -= 1
        elif dir == 'L':
            dir = 'D'
            x += 1
        elif dir == 'U':
            dir = 'R'
            y += 1
        else:
            dir = 'U'
            x -= 1
    else:
        if dir == 'D':
            dir = 'R'
            y += 1
        elif dir == 'L':
            dir = 'U'
            x -= 1
        elif dir == 'U':
            dir = 'L'
            y -= 1
        else:
            dir = 'D'
            x += 1
    cnt += 1

print(cnt)