import sys
from collections import deque

# testcase 개수
t=int(sys.stdin.readline())
for _ in range(t):
    # 편의점 개수
    n = int(sys.stdin.readline())
    # 이동거리 안에 있는 좌표
    graph=[]
    # 상근집 x,y 좌표
    sgx, sgy=map(int, sys.stdin.readline().split(' '))
    # 편의점 좌표
    cu=[]
    for _ in range(n):
        cux, cuy = map(int, sys.stdin.readline().split(' '))
        cu.append([cux, cuy])
        graph.append([cux, cuy])
    # 페스티벌 좌표
    fex, fey=map(int, sys.stdin.readline().split(' '))
    # 노드간의 거리가 1000 이하면 이동 가능
    queue=deque()
    queue.append([sgx, sgy])
    # 편의점 좌표 인덱스 + 최종 목적지 인덱스를 기준으로 visited 배열 체크
    visited=[0]*(n)
    isHappy=False
    while queue:
        curx, cury=queue.popleft()
        # 해당 좌표와 페스티벌 거리가 1000이하 이면 성공
        if abs(curx-fex)+abs(cury-fey)<=1000:
            isHappy=True
            break
        for i in range(n):
            if visited[i]==0:
                # 방문한 적 없는 i번째 순서이면 계산해보고, curx, cury와의 맨해튼 거리가 1000 이하면 queue에 append
                x,y=cu[i]
                distance=abs(curx-x)+abs(cury-y)
                if distance<=1000:
                    queue.append([x,y])
                    visited[i] = 1
    # 기존의 visited에 0이 있으면, 즉 방문하지 않은 노드가 있으면 sad를 출력하던 방식은 잘못됐음
    if isHappy:
        print("happy")
    else:
        print("sad")


