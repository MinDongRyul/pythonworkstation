#플로이드 워셜 알고리즘 점화식
#for k in range(1, n + 1):
#    for a in range(1, n + 1):
#        for b in range(1, n + 1):
#            graph[a][b] = min(graph[a][b], \
#                graph[a][k] + graph[k][b])
# a b : 간선, k : 최종 목적지