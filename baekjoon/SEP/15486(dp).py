import sys

n=int(sys.stdin.readline())
T=[0]
P=[0]
# DP[n] => n-1일째까지 받을 수 있는 최대 금액
DP=[0]*(n+2)
for idx in range(n):
    t,p=map(int, sys.stdin.readline().strip().split(' '))
    T.append(t)
    P.append(p)

curMax=0
for i in range(1,n+1):
    # 정산일
    payday=i+T[i]
    # 현재까지 가장 큰 값이 몇인지 갱신 (현재 인덱스의 값이 가장 큰 값일 수 있으므로, payday DP 갱신 전에 curMax를 갱신해준다)
    curMax=max(curMax, DP[i])
    if payday<=n+1:
        # N+1일째 되는 날까지 정산될 수 있는 경우 해당 날짜의 DP 값 갱신
        DP[payday]=max(DP[payday], curMax+P[i])

print(max(DP))