import sys

t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    score=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(2)]

    # dp[i][j] = 해당 위치에서 얻을 수 있는 점수의 최대 합
    dp=[[0]*(n) for _ in range(2)]
    dp[0][0]=score[0][0]
    dp[1][0]=score[1][0]

    for idx in range(1,n):
        # 1번 인덱스의 경우, 각 시작점에서 대각선으로 이동하는 경우만 가능하다.
        if idx==1:
            dp[1][idx]=dp[0][0]+score[1][idx]
            dp[0][idx]=dp[1][0]+score[0][idx]
            continue
        # 각 위치에 저장될 수 있는 점수의 최댓값을 계산한다.
        # 각 위치에서 올 수 있는 경우는 두 가지이다.
        # 1) 바로 이전 열의 대각선 방향에서 오는 경우
        # 2) 두 열 이전의 대각선 방향에서 오는 경우
        # 두 경우 중 더 큰 dp 값을 가지는 경우를 선택한다.
        dp[0][idx]=max(dp[1][idx-1], dp[1][idx-2])+score[0][idx]
        dp[1][idx]=max(dp[0][idx-1], dp[0][idx-2])+score[1][idx]
    # 0행 0열에서 시작해서 마지막까지 도달한 경우와 1행 0열에서 시작해서 마지막까지 도달한 경우를 비교해서 더 큰 값을 출력한다.
    print(max(dp[0][n-1], dp[1][n-1]))
