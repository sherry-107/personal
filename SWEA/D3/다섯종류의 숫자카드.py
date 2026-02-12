num = list(map(int, input()))
cnt = 0

def func(level, num):
    global cnt
    if level == 4:
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i-1]) > 3:
                return
        cnt += 1
        return
    for i in num:
        arr.append(i)
        func(level+1, num)
        arr.pop()

arr = []

func(0, num)
print(cnt)