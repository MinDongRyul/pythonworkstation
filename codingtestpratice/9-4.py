from turtle import distance


INF = int(1e9)
n, m = map(int, input().split())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한을 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 길은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 간선 정보 받기
for _ in range(1, m):
    # a 와 b가 서로에게 가는 비용은 1이라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 K를 입력 받기
x, k = map(int, input().split())

# 점화식에 따라 플로이들 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], \
                graph[a][k] + graph[k][b])

# 수행된 결과를 출력
# 1번 부터 시작하여 k를 거쳐 x까지 가는 최단 경록 구하기
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1 출력
if distance >= INF:
    print("-1")
else:
    print(distance)