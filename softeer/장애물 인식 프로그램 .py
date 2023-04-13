import sys
from collections import deque

n = int(sys.stdin.readline())
area = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

block = 0
number = []


def bfs(i, j):
    global visited, area
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cnt = 1
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1
    while queue:
        y, x = queue.popleft()
        for di in directions:
            dy = y + di[0]
            dx = x + di[1]
            if 0 <= dy < n and 0 <= dx < n and visited[dy][dx] == 0 and area[dy][dx] == 1:
                cnt += 1
                queue.append((dy, dx))
                visited[dy][dx] = 1
    return cnt


for i in range(n):
    for j in range(n):
        # 장애물이면서, 방문하지 않은 경우
        if area[i][j] == 1 and visited[i][j] == 0:
            block += 1
            number.append(bfs(i, j))

print(block)
number.sort()
for num in number:
    print(num)
