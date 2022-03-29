# for문 중첩 시간 초과 판정 예상
n, m = map(int, input().split())
kg = list(map(int, input().split()))
count = 0
for i in range(0, len(kg) - 1):
    for j in range(i + 1, len(kg)):
        if kg[i] != kg[j]:
            count += 1
print(count) 

# 모범 답안
# n, m = map(int, input().split())
# data = list(map(int, input().split()))

#  1부터 10까지의 무게를 담을 수 있는 리스트
# array = [0] * 11

# for x in data:
#      각 무게에 해당 되는 볼링공의 개수 카운트
#      array[x] += 1

# result = 0
#  1부터 m까지의 무게에 대하여 처리
# for i in range(1, m + 1):
#     n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
#     result += array[i] * n # B가 선택하는 경우의 수와 곱하기

# print(result)
