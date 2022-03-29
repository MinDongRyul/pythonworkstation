n = int(input())
travel = list(map(int, input().split()))
travel.sort()
print(travel)
sum = 0
count = 0
for i in travel:
    sum += 1
    if sum >= i:
        count += 1
        sum = 0
print(count)