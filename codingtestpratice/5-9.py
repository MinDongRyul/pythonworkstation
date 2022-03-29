n, k = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input()))) #  공백 없이 한줄로 리스트 받기

def dfs(x, y):
    # 주어진 범위가 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= k:
        return False

    if array[x][y] == 0: 
        # 처음 들어온게 0 이라면 무조건 True 리턴후 sum 1 증가
        
        array[x][y] = 1

        # 상 하 좌 우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y) 
        dfs(x, y - 1) 
        dfs(x + 1, y) 
        dfs(x, y + 1) 
        return True
    return False

# 모든 노드에 대하여 음료수 채우기
sum = 0
for i in range(n):
    for j in range(k): 
        if dfs(i, j) == True:
            sum += 1

print(sum)
