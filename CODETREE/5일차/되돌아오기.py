N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

x = 0
y = 0

idx = -1
cnt = 0

for i in range(N):
    for j in range(dist[i]):
        if dir[i] == 'N':
            y += 1
        elif dir[i] == 'E':
            x += 1
        elif dir[i] == 'S':
            y -= 1
        else:
            x -= 1
        cnt += 1
        if x == 0 and y == 0:
            idx = cnt
            break
    if idx == cnt:
        break
        

print(idx)
    