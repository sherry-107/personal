t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())

    ans_arr = list(map(int, input().split()))
    stu_arr = [list(map(int, input().split())) for i in range(n)]
    score_arr = []

    for student in stu_arr:
        if student[0] == ans_arr[0]:
            score_sum = 1
        else:
            score_sum = 0

        for i in range(1, m):
            score = 0
            if student[i] == ans_arr[i]:
                for j in range(0, i):
                    if student[j] == ans_arr[j]:
                        score += 1
                    else:
                        score = 0
                score_sum += score + 1
        score_arr.append(score_sum)
    
    print(f'#{tc}', max(score_arr) - min(score_arr))