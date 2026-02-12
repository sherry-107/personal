txt = input()
find_txt = input()


arr = []
index = 0
arr2 = []

for i in range(0, len(txt) - len(find_txt)):
    cnt = 0
    k = 0
    while k < len(find_txt):
        if find_txt[k] != txt[i+k]:
            break
        else:
            cnt += 1

        if cnt == len(find_txt):
            arr.append(i)
            cnt = 0
        k += 1
            
print(len(arr))

for i in arr:
    i = i + 1
    arr2.append(i)
    

print(*arr2)
            


