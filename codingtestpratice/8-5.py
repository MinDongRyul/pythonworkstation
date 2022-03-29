n = int(input())

d = [0] * 30001

# 다이나믹 프로그래밍 (보텀업) 
for i in range(2, n + 1):
    d[i] = d[i - 1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1) # +1 하는이유 : 함수의 호출 횟수를 구해야하기 때문
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[n])
    