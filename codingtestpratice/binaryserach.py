from bisect import bisect_left, bisect_right
# 값이[left_value, right_value]인 데이터의 개수를 반환하는 함수
def count(dduk, left_value, right_value):
    right_index = bisect_right(dduk, right_value)
    left_index = bisect_left(dduk, left_value)
    print(right_index, left_index)
    return right_index - left_index
    
n, k = map(int, input().split())# k의 개수 출력
dduk = list(map(int, input().split()))

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count_k = count(dduk, k, k)
if count_k == 0:
    print(-1)
else:
    print(count_k)