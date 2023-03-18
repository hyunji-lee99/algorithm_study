# dfs? ㄴㄴ 구현
# 재귀식으로 dfs쓰면 런타임에러 발생
# 코딩테스트 대비 라이브러리 사용 X

n,m=map(int, input().split(' '))
# 초기 로봇청소기 위치
startr, startc, startd =map(int, input().split(' '))

area=[]
for i in range(n):
    tmp=list(input().split(' '))
    area.append(tmp)

# 북 동 남 서 / 0 1 2 3
directions=[(-1,0),(0,1),(1,0),(0,-1)]
cleanok=[[0]*m for _ in range(n)]
curr=startr
curc=startc
curd=startd
mass=0
while True:
    # 현재 칸이 청소되어 있지 않은 경우, 청소한다
    if area[curr][curc]=='0' and cleanok[curr][curc]==0:
        mass+=1
        cleanok[curr][curc]=1
    # 현재 칸에서 이동할 수 있는 칸이 있는지 탐색한다
    for di in directions:
        dy=curr+di[0]
        dx=curc+di[1]
        if 0<=dy<n and 0<=dx<m and area[dy][dx]=='0' and cleanok[dy][dx]==0:
            # 반시계 방향 이동 계산
            dir=curd
            if curd==0:
                dir=3
            elif curd==1:
                dir=0
            elif curd==2:
                dir=1
            elif curd==3:
                dir=2
            newy=curr+directions[dir][0]
            newx=curc+directions[dir][1]
            if 0<=newy<n and 0<=newx<m and area[newy][newx]=='0' and cleanok[newy][newx]==0:
                curr=newy
                curc=newx
                curd=dir
            else:
                curd=dir
            break
    else:
        # 이동할 수 있는 곳이 없는 경우
        dy=curr+directions[curd-2][0]
        dx=curc+directions[curd-2][1]
        if 0<=dy<n and 0<=dx<m:
            if area[dy][dx]=='1':
                print(mass)
                exit(0)
            elif area[dy][dx]=='0':
                curr=dy
                curc=dx