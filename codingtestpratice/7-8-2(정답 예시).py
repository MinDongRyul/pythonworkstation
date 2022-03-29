n, k = map(int, input().split())
ddeok = list(map(int, input().split()))

start = 0
end = max(ddeok)
while (start <= end):
    mid = (start + end) // 2
    sum = 0
    for i in ddeok:
        if i > mid:
            sum += (i - mid)

    if sum == k :
        result = mid
        break
    elif sum > k:
        start = mid + 1
    else :
        end = mid - 1
    
print(result)