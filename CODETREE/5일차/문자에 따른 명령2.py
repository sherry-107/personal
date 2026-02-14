dirs = input()

# Please write your code here.

dir = 'N'

L_arr = ['N', 'W', 'S', 'E', 'N']
R_arr = ['N', 'E', 'S', 'W', 'N']

x , y = 0, 0

for i in dirs:
    if i == 'L':
        for j in range(0, 4):
            if L_arr[j] == dir:
                dir = L_arr[j+1]
                break
    elif i == 'R':
        for j in range(0, 4):
            if R_arr[j] == dir:
                dir = R_arr[j+1]
                break

    else:
        if dir == 'N':
            y += 1
        elif dir == 'W':
            x -= 1
        elif dir == 'S':
            y -= 1
        else:
            x += 1



print(x, y)