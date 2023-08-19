import sys

n,a,b=map(int, sys.stdin.readline().split(' '))
# 건물의 최고 높이는 max(a,b)
maxheight=max(a,b)
# a-1까지 오름차순 + 최고 건물 높이 + b-1부터 내림차순
buildings=list(range(1,a))+[maxheight]+list(range(b-1,0,-1))

# 만들어진 건물들의 개수가 n보다 크다면 불가능한 경우
if len(buildings)>n:
    print(-1)
    sys.exit(0)

# n보다 작다면 가희가 볼 수 있는 건물의 개수를 위반하지 않으면서 사전순으로 가장 앞쪽에 위치한 건물 배열을 만들기 위해서
# 1을 넣을 수 있는 만큼 왼쪽에 넣어준다
# insert(0,1) 아니고 insert(1,1)이어야 함
# 반례 : 3 1 2
while len(buildings)<n:
    buildings.insert(1,1)

for b in range(n):
    print(buildings[b], end=' ')
