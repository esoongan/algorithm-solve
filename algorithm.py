def solution(n, s, a, b, fares):
    answer = [0] * (n+1)
    # s - 출발지점, a,b각각 도착지점
    graph = [ [0 for _ in range(n+1)] for _ in range(n+1)]
    INF = int(1e9)

    for i in fares:
        start, end, cost = i[0], i[1], i[2]
        graph[start][end] = cost
        graph[end][start] = cost

    for i in range(1, n+1):
        distance = [INF] * (n + 1)
        visited = [False] * (n + 1)

        answer[i] = digkstra(i, visited, distance, graph, n)

    # 중간지점이 1~n
    result = 1e9
    for i in range(1,n+1):
        # 시작점 ~ 중간지점 + 중간지점 ~ a + 중간지점 ~ b
        result = min(result, answer[s][i] + answer[i][a] + answer[i][b])

    return result

def digkstra(start, visited, distance, graph,n):
    #방문처리
    visited[start] = True
    distance[start] = 0

    for idx, i in enumerate(graph[start]):  # 현재노드로부터 연결된 노드를 찾음
        if i != 0:  # 연결되어있다는것
            temp = i + distance[start]  # 현재노드까지의 거리 + 현재로부터 목적지노드까지의 거리
            if temp < distance[idx]:
                distance[idx] = temp  # 더 최단거리이면 갱신

    # 시작노드를 제외한 나머지노드에서 반복
    for _ in range(n-1):
        # distance에서 방문전이면서 가장작은 노드의 인덱스를 찾는다.
        min_val = int(1e9)
        min_idx = 0
        for i in range(n+1):
            if distance[i] < min_val and not visited[i]:
                min_val, min_idx = distance[i], i

        visited[min_idx] = True

        for idx, j in enumerate(graph[min_idx]):
            if j != 0:
                temp = j + distance[min_idx]  # 현재노드까지의 거리 + 현재로부터 목적지노드까지의 거리
                if temp < distance[idx]:
                    distance[idx] = temp  # 더 최단거리이면 갱신
    return distance

solution(6,4,6,2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])