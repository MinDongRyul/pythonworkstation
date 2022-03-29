s = list(input())
array = []
sum = 0
for i in s:
    if i.isalpha():
        array.append(i)
    else:
        sum += int(i)
array.sort()
if sum != 0 :
    array.append(str(sum)) # 0인 경우 : 처음 문자열 s에 숫자가 없는경우
print("".join(array))

