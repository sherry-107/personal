n = int(input())

arr = list(map(int, input().split()))

result = 0

while len(arr) != 1:
    arr.sort()
    v1, v2 = arr.pop(0), arr.pop(0)

    result += v1 + v2
    arr.append(v1+v2)

print(result)