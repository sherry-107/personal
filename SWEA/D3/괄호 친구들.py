text = input()

sum = 0

idx1 = 0
idx2 = 0

while idx1 != -1 or idx2 != -1:
    idx1 = text.find('[')
    idx2 = text.find('{')

    if (idx1 < idx2 and idx1 != -1) or (idx1 > idx2 and idx2 == -1):
        end1 = text.find(']')
        num = int(text[idx1+1:end1])
        text = text[end1+1:]

        sum += num

    if (idx1 > idx2 and idx2 != -1) or (idx1 < idx2 and idx1 == -1):
        end2 = text.find('}')
        num = int(text[idx2+1:end2])
        text = text[end2+1:]

        sum *= num

print(sum)
