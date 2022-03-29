n, k  = map(int, input().split())
money =[]
score, num = 0, n-1
for i in range(n):
    j = int(input())
    money.append(j)
money.sort(reverse=True)
#while k > 0:
#    if k >= money[num]:
#        k -= money[num]
#        score += 1
#    else :
#        num -= 1 
for coin in money:
    score += k
    k %= coin
print(score)
