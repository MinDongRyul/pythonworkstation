def binary_search(array, target, start, end):
    
    if start > end :
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target :
        binary_search(array, target, start, mid - 1)
    else:
        binary_search(array, target, mid + 1, end)
    
n = int(input())
array = list(map(int, input().split()))

k = int(input())
item = list(map(int, input().split()))

array.sort()

for i in item:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")