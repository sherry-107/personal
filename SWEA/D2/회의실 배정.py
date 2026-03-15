n = int(input())

meeting = []

end = 0
cnt = 0

for i in range(n):
    a, b = map(int, input().split())
    meeting.append([b, a])
    end = max(end, b)

meeting.sort()

for i in range(n):
    meeting[i][0], meeting[i][1] = meeting[i][1], meeting[i][0]

dat = [0] * (end+1)

for a, b in meeting:
    idx = True
    for i in range(a, b):
        if dat[i] != 0:
            idx = False
        
    if idx:
        for i in range(a, b):
            dat[i] = 1
        cnt += 1

print(cnt)