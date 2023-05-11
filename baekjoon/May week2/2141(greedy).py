# 우체국의 위치를 X라 하고, X를 기준으로 좌우에 퍼져있는 우체국의 수가 비슷할 수록 각 사람들까지의 거리 합이 최소가 됨
# 마을 사람들의 총합을 구하고, 그 수의 절반을 넘어가는 위치인 순간이 정답이 됨.

import sys

n=int(sys.stdin.readline())
info=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
total_polulation=sum([x[1] for x in info])
info.sort(key=lambda x:x[0])

# 누적합
score=0
# //로 하지말고 /로 소수점까지 처리해줘야 함
target=total_polulation/2
for pos, popul in info:
    if score+popul>=target:
        print(pos)
        sys.exit(0)
    else:
        score+=popul
