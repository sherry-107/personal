N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.

idx = -1
dict = {}

for i in range(1, N+1):
    dict[i] = 0

for i in student:
    dict[i] += 1
    if dict[i] == K:
        idx = i
        break
    

print(idx)