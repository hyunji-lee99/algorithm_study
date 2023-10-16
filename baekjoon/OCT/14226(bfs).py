import sys
from collections import deque

s=int(sys.stdin.readline())

# init queue
queue=deque()
# 화면에 표시된 이모티콘 개수, 클립보드에 저장된 이모티콘 개수, 소요 시간
queue.append((1, 0, 0))
# 방문 표시
visited=set((1,0,0))

while queue:
    m, c, t = queue.popleft()
    if m==s:
        print(t)
        break
    # 1) 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
    if m>0 and (m, m, t+1) not in visited:
        queue.append((m, m, t+1))
        visited.add((m, m, t+1))
    # 2) 클립보드에 있는 이모티콘을 화면에 붙여넣기
    if c>0 and (m+c, c, t+1) not in visited:
        queue.append((m+c, c, t+1))
        visited.add((m+c, c, t+1))
    # 3) 화면에 있는 이모티콘 1개 삭제
    if m>0 and (m-1, c, t+1) not in visited:
        queue.append((m-1,c,t+1))
        visited.add((m-1,c,t+1))
