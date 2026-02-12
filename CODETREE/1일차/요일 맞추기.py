m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

day_dict = {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu', 4:'Fri', 5:'Sat', 6:'Sun'}
month_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

start = d1
end = d2

for i in range(1, m1):
    start += month_dict[i]

for i in range(1, m2):
    end += month_dict[i]

diff = end - start

print(day_dict[diff%7])