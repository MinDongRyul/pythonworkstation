n = input()
sum = int(n[0])
for i in range(1, len(n)):
    num = int(n[i])
    if num <= 1 or sum <= 1:
        sum += num
    else:
        sum *= num

print(sum)

# 모범답안
# data = input()

# result = int(data[0])

# for i in range(1, len(data)):
#     num = int(data[i])
