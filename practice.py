print(5%796796)
print(3%2)

# 리스트 컴프리헨션
# i값을 바로 리스트에 넣어주기
# array = [i for i in range(20) if i % 2 ==1] 
# print(array)

# 2차원 리스트 초기화 n X m 크기
# array = [[0] * m for _ in range(n)]

# 잘못된 예시
# array = [[0] * m] * n

# 유니코드 변환
# ord('문자') -> 유니코드
# chr(유니코드) -> '문자'

# x.isalpha()
# x가 알파벳인지 확인해주기

# DFS 메서드 정의
# def dfs(graph, v, visited):
#     # 현재 노드를 방문 처리
#     visited[v] = True
#     print(v, end=' ')
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, v, visited)

# from collections import deque
# BFS 메서드 정의 (최단 거리)
# 
# def bfs(graph, start, visited):
#     # 큐 구현을 위해 deque 라이브러리 사용
#     queue = deque([start])
#     # 현재 노드를 방문 처리
#     visited[start] = True 
#     # 큐가 빌 때까지 반복
#     while queue:
#         # 큐에서 하나의 원소를 뽑아 출력
#         v = queue.popleft()
#         print(v, end=' ')
#         # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
#         for i in graph[v]:
#             if not visited[i]:
#             queue.append(i)
#             visited[i] = True

# 3 if else
# [True1] if [Condition1] else [True2] if [Condition2] else [False]

#if [Condition1]:
#    [True1]
#elif [Condition2]:
#    [True2]
#else
#    [False]

# 2차원 배열에서 방향전환이 필요할 때
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# 배열 입력시 입력값이 한줄로 들어왔을 때 나누어 주는 방법
# array 입력 값 : 1 0 0 0 3 4 1 2 1 6 5 5
# dp.append(array[index:index + m]) m : 나누어 주고싶은구간
#     index += m # 4 다음 8 다음 12
# array = [[1, 0, 0, 3], 
#          [3, 4, 1, 2], 
#          [1, 6, 5, 5]
#          ]