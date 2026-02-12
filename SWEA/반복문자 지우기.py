t = int(input())

for tc in range(1, t+1):
    text = input()
    stack = []

    for i in text:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    print(f'#{tc}', len(stack))