n, m = map(int, input().split()) # n : arr크기, m : 정신력 수치
L = int(input())
text = input()
arr = [list(map(int, input().split())) for i in range(n)]

x, y = 0, 0

idx = 'Y'

for i in range(L):
    x1, y1 = 0, 0
    if text[i] == 'U':
        x1 -= 1
    elif text[i] == 'L':
        y1 -= 1
    elif text[i] == 'R':
        y1 += 1
    else:
        x1 += 1

    if x + x1 < 0 or x + x1 >= n or y + y1 < 0 or y + y1 >= n:
        continue
    else:
        x += x1
        y += y1

        m -= arr[x][y]
    if m <= 0:
        break

if i < L-1:
    idx = 'N'

print(idx)
print(x + 1, y + 1)