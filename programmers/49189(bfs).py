from collections import deque

n=6
edge=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
def solution(n, edge):
    answer = 0
    # graph init
    graph = [[] for _ in range(n + 1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    # visited, queue, distance init
    visited = [0] * (n + 1)
    distance = [0] * (n + 1)
    queue = deque()
    visited[1] = 1
    queue.append(1)

    # bfs
    while queue:
        cur = queue.popleft()
        for node in graph[cur]:
            if visited[node] == 0:
                queue.append(node)
                visited[node] = 1
                distance[node] = distance[cur] + 1
    maxlength = max(distance)
    # (!!) count 함수
    answer = distance.count(maxlength)
    return answer

print(solution(n,edge))