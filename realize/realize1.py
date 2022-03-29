n = list(map(int, input()))
m = list(n[0:len(n)//2])
k = list(n[len(n)//2:])
if sum(m) - sum(k) == 0:
    print("LUCKY")
else:
    print("READY")

# n = input()
# m = len(n)

# sum = 0

# for i in range(m//2):
#     sum += int(n[i])

# for i in range(m//2, m):
#     sum -= int(n[i])

# if sum == 0 :
#     print("LUCKY")
# else:
#     print("READY")