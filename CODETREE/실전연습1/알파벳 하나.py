n = int(input())
arr = [list(map(str, input())) for i in range(n)]
dict = {}
max_v = 0
alpha = 'Z'

for i in arr:
    for j in i:
        dict[j] = 0

for i in arr:
    for j in i:
        dict[j] += 1
        max_v = max(max_v, dict[j])

for key, value in dict.items():
    if value == max_v:
        if key < alpha:
            alpha = key

print(n*n-max_v, alpha)