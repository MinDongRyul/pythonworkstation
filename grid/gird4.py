n = int(input())
money = list(map(int, input().split()))
money.sort()

target = 1
for i in money:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < i:
        break
    target += i

# 만들 수 없는 금액 출력
print("최종" + str(target))