t = int(input())

for tc in range(1, t+1):
    arr = list(map(str, input().split()))
    stack = []

    for i in arr:
        if i in '+-*/':
            if len(stack) < 2:
                result = 'error'
                break
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if i == '+':
                    calc = num1 + num2
                elif i == '-':
                    calc = num1 - num2
                elif i == '*':
                    calc = num1 * num2
                else:
                    calc = num1 // num2
                stack.append(str(calc))
        elif i == '.':
            if len(stack) == 1:
                result = stack.pop()
            else:
                result = 'error'
        else:
            stack.append(i)
            
    print(f'#{tc}', result)