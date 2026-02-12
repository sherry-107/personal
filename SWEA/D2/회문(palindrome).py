t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [input() for i in range(n)]
    arr2 = []

    for i in range(n):
        for j in range(n-m+1):
            if arr[i][j:j+m] == arr[i][j:j+m][::-1]:
                print(f'#{tc}', arr[i][j:j+m])

    for i in range(n):
        text = ''
        for j in range(n):
            text += arr[j][i]
        
        arr2.append(text)

    for i in range(n):
        for j in range(n-m+1):
            if arr2[i][j:j+m] == arr2[i][j:j+m][::-1]:
                print(f'#{tc}', arr2[i][j:j+m])