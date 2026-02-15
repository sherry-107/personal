n, k = map(int, input().split())
text = input()

forbid = [tuple(map(int, input().split())) for i in range(k)]

x, y = 0, 0


for i in text:
    x1, y1 = 0, 0
    if i == 'W':
        x1 -= 1
    elif i == 'A':
        y1 -= 1
    elif i == 'S':
        x1 += 1
    else:
        y1 += 1

    if (x + x1 < 0 or x + x1 > 30000) or (y + y1 < 0 or y + y1 > 30000) or ((x + x1, y + y1) in forbid):
        continue
    else:
        x += x1
        y += y1

print(x, y)
