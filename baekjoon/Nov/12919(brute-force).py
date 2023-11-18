import sys
from collections import deque

S=sys.stdin.readline().strip()
T=sys.stdin.readline().strip()

# S에서 시작해서 T가 가능한지 확인하려면 최대 2^50 시간복잡도가 필요해서 시간 초과 발생할 수 있음
# T에서 하나씩 소거하면서 S가 될 수 있는지 파악해야 함

queue=deque([T])
visited=set()

while queue:
    cur=queue.popleft()
    # 연산 취소 과정에서 길이가 0인 문자열 발생함
    if len(cur)==0:
        continue
    if cur==S:
        print(1)
        sys.exit()
    # 1번 연산 (뒤에 A를 추가하는 연산)을 취소할 수 있는가?
    if cur[-1]=='A':
        removeA=cur[:-1]
        # 아직 방문한 적 없다면
        if removeA not in visited:
            queue.append(removeA)
            visited.add(removeA)
    # 2번 연산 (B를 추가하고 뒤집는 연산)을 취소할 수 있는지?
    if cur[0]=='B':
        removeB=cur[-1:0:-1]
        if removeB not in visited:
            queue.append(removeB)
            visited.add(removeB)
else:
    print(0)
