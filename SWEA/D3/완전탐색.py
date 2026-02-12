t = int(input())
cnt = 0

def func(level, t):
    global cnt
    if level == t:
        if sum(arr) <= 10:
            cnt += 1
        return
    for i in range(1, 7):
        arr.append(i)
        func(level + 1, t)
        arr.pop()

arr = []

func(0, t)
print(cnt)
