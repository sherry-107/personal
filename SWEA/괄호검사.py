t = int(input())

for tc in range(1, t+1):
    text = input()
    stack = []
    result = 1

    for i in text:
        if i in '({[':
            stack.append(i)
        if i in ')}]':
            if len(stack) == 0:
                result = 0
                break
            elif i == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    result = 0
                    break
            elif i == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    result = 0
                    break
            elif i == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    result = 0
                    break
    if result == 1 and len(stack) == 0:
        print(f'#{tc}', result)
    else:
        print(f'#{tc}', 0)