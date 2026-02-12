#부분 문자열

txt = input()
find_txt = input()

a = 0

for i in range(len(txt) - len(find_txt) + 1):
    cnt = 0
    for j in range(len(find_txt)):
        if find_txt[j] == txt[j+i]:
            cnt +=1

        if cnt == len(find_txt):
            a = 1

print(a)