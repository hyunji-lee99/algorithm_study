# n*n
n=int(input())
# 뱀이 기어다닐 지도를 하나 만듬(dummy 포함)
area=[[0]*(n+1) for _ in range(n+1)]
# 사과의 개수 k
k=int(input())
# 다음 k줄엔 사과의 위치
for i in range(k):
    i,j=map(int, input().strip().split(' '))
    # 사과는 지도상에 2로 표시
    area[i][j]=2
# 뱀의 방향 변환 횟수 l
# x c -> 게임 시작 후 x초가 끝난 뒤에 왼쪽(L) 또는 오른쪽(D)로 90도 회전한다는 뜻
l=int(input())
change=[]
for i in range(l):
    x,c=input().strip().split(' ')
    change.append((int(x),c))

# head, tail 위치 init
# 현재 뱀이 차지하고 있는 위치 저장할 배열
head=(1,1)
tail=(1,1)
snake=[(1,1)]

# 북, 동, 남, 서
directions=[(-1,0),(0,1),(1,0),(0,-1)]
time=0
# 벰은 처음에 오른쪽으로 이동함
dir=1
while True:
    if change:
        if time == change[0][0]:
            # 오른쪽으로 90도 회전
            if change[0][1] == 'D':
                if dir == 3:
                    dir = 0
                else:
                    dir += 1
            # 왼쪽으로 90도 회전
            elif change[0][1] == 'L':
                if dir == 0:
                    dir = 3
                else:
                    dir -= 1
            change.pop(0)
    hy,hx=snake[-1]
    time+=1
    # 몸길이를 늘려 다음 칸에 머리 위치
    hdy=hy+directions[dir][0]
    hdx=hx+directions[dir][1]

    if 1<=hdy<=n and 1<=hdx<=n:
        # 뱀이 스스로 부딪히면
        if (hdy, hdx) in snake:
            print(time)
            break
        snake.append((hdy,hdx))
        # 이동한 칸의 사과가 없다면 꼬리칸 비움
        if area[hdy][hdx]==0:
            snake.pop(0)
        # 이동한 칸의 사과가 있을 경우
        elif area[hdy][hdx]==2:
            # 길이만 늘려주고, 사과는 삭제해야 함
            area[hdy][hdx]=0
    else:
        # 범위를 벗어나면
        print(time)
        break

