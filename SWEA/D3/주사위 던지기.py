t = int(input())

def func(level, t, start):
    if level == t:
        print(*arr)
        return

    for i in range(start, 7):
        arr.append(i)
        func(level+1, t, i)
        arr.pop()

arr = []

func(0, t, 1)
