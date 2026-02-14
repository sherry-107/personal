n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.


x = r
y = c

for i in range(t):
    if d == 'L':
        y -= 1
        if y < 1 or y > n:
            y += 1
            d = 'R'
    elif d == 'R':
        y += 1
        if y > n or y < 1:
            y -= 1
            d = 'L'
    elif d == 'U':
        x -= 1
        if x < 1 or x > n:
            x += 1
            d = 'D'
    else:
        x += 1
        if x > n or x < 1:
            x -= 1
            d = 'U'

print(x, y)