commands = input()

# Please write your code here.

x = 0
y = 0
cnt = 0
idx = -1
dir = 'N'

L_arr = ['N', 'W', 'S', 'E', 'N']
R_arr = ['N', 'E', 'S', 'W', 'N']

for command in commands:
    if command == 'L':
        for i in range(4):
            if L_arr[i] == dir:
                dir = L_arr[i+1]
                break

    elif command == 'R':
        for i in range(4):
            if R_arr[i] == dir:
                dir = R_arr[i+1]
                break

    else:
        if dir == 'N':
            y += 1
        elif dir == 'E':
            x += 1
        elif dir == 'W':
            x -= 1
        else:
            y -= 1
    cnt += 1

    if x == 0 and y ==0 :
        idx = cnt
        break

print(idx)
