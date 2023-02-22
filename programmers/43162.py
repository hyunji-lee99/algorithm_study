from collections import deque

n=3
computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
def solution(n, computers):
    answer = 0
    # visited,queue,network init
    network = 0
    visited = [0] * n
    queue = deque()
    queue.append(0)
    visited[0] = 1
    # n=1일 때, 즉 네트워크 노드가 1개인 경우는 기존 알고리즘대로 하면 while문 안으로
    # 아예 들어가질 못해서 네크워크 개수가 0개인 것으로 리턴됨.
    if n == 1:
        return 1
    # (!!) in 구문 실수 주의
    while 0 in visited:
        while queue:
            cur = queue.popleft()
            # 밖에 있어야 for문 안에서 조건에 해당되지 않아도 처리 가능
            visited[cur] = 1
            for i in range(len(computers[cur])):
                # 자기자신이 아니면서, 연결되어있고, 방문한 적 없는 노드일 경우
                if i != cur and computers[cur][i] == 1 and visited[i] == 0:
                    queue.append(i)
        network += 1
        # 아직 방문하지 않은 다른 노드 추가
        for j in range(len(visited)):
            if visited[j] == 0:
                queue.append(j)
                break
    return network

print(solution(n,computers))