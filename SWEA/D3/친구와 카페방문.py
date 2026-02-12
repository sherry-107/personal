text = list(map(str, input().split()))
cnt = 0

def func(level, length):
    global cnt
    if level == length:
        if sum(arr) >= 2:
            cnt += 1
        return
    for i in range(0, 2):
        arr.append(i)
        func(level+1, length)
        arr.pop()


arr = []
length = len(text)
func(0, length)

print(cnt)