text = ['GOLDABCGOLD', 'HELLOWORLD', 'WHITEGOLD']

cnt = 0
index = 0

while index < len(text):
    find_idx = text[index].find('GOLD')

    if find_idx != -1:
        end_idx = find_idx + len('GOLD')
        text[index] = text[index][end_idx:]
        cnt += 1

    else:
        index += 1

print(cnt)

