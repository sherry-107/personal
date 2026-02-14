n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

x = 0
y = 0

for i in range(n):
    if dir[i] == 'E':
        x += dist[i]
    elif dir[i] == 'W':
        x -= dist[i]
    elif dir[i] == 'S':
        y -= dist[i] 
    else:
        y += dist[i]

print(x, y)