def binary(ddeok, k, start, end):
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for i in ddeok:
            m = i - mid
            if m < 0 :
                continue
            sum += m
        if sum == k :
            return mid
        elif sum > k:
            start = mid + 1
        else :
            end = mid - 1
    return None

n, k = map(int, input().split())
ddeok = list(map(int, input().split()))

result = binary(ddeok, k, 0, max(ddeok))
print(result)