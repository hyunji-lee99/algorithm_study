# 모든 격자판을 L*L 사이즈 2차원 배열로 나눠서 완전탐색하는 것이 아니라, (n,m이 최대 50만이기 때문에 시간초과 발생함)
# 각 별들을 트램펄린의 가장자리에 위치한다 가정하고 모든 별을 기준으로 트램펄린의 위치를 정했을 때, 각각 몇 개의 별을 튕겨내야 하는지 완전탐색하면 됨. (별의 개수 K는 최대 100)
# (x,y)로 주어지며 n이 가로 길이, m이 세로 길이인 것 주의

import sys

n,m,l,k=map(int, sys.stdin.readline().split(' '))

stars=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(k)]

maxvalue=-1e9
for i in range(k):
    for j in range(k):
        # 모서리 두 개의 별을 포함하는 경우
        # 첫 번째 별에서 X 추출
        x=stars[i][0]
        # 두 번째 별에서 Y 추출
        y=stars[j][1]
        cnt=0
        for dx,dy in stars:
            if x<=dx<=x+l and y<=dy<=y+l:
                cnt+=1
        maxvalue=max(maxvalue, cnt)

# 지구로 떨어지는 별의 개수 = 전체 떨어지는 별의 개수 - 우주로 튕겨낸 별의 개수 최댓값
print(k-maxvalue)
