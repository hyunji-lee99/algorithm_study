import sys

t=int(sys.stdin.readline())


# idx : idx번째 포지션에 올 선수 저장
# total : 총 능력치
def DFS(idx, total):
    global maxans
    if idx == 11:
        maxans = max(maxans, total)
        return

    for p in range(11):
        # 이미 포지션에 배치된 선수이거나 선수가 해당 포지션의 능력치가 0인 경우, 다음 선수 탐색
        if visited[p] == 1 or player[p][idx] == 0:
            continue
        visited[p] = 1
        total += player[p][idx]
        DFS(idx + 1, total)
        total -= player[p][idx]
        visited[p] = 0

for _ in range(t):
    player=[]
    # input
    for i in range(11):
        power=list(map(int, sys.stdin.readline().split(' ')))
        player.append(power)
    visited=[0]*(11)
    maxans=0
    DFS(0,0)
    print(maxans)
