import sys

n,m,t=map(int, sys.stdin.readline().split(' '))
# dummy
circle=[[0]*(n+1)]+[[0]+list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
command=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(t)]

def rotate(x,d,k):
    global circle, n
    # 번호가 x의 배수인 원판은 d방향으로 k칸 회전시킴
    for i in range(1,n+1):
        if i%x==0:
            tmp_circle=circle[i].copy()
            # 시계 방향으로 k칸 회전
            if d==0:
                for cnt in range(k):
                    last = tmp_circle.pop()
                    tmp_circle.insert(1, last)
            elif d==1:
                for cnt in range(k):
                    first = tmp_circle.pop(1)
                    tmp_circle.append(first)
            circle[i]=tmp_circle.copy()

def find_adjacent():
    global circle, n,m
    directions=[(1,0),(0,1),(0,-1),(-1,0)]
    isExist = False
    isZero=False
    sumCircle=0
    numCircle=0
    # 계산 과정에서 circle 값이 직접 바뀌면서 생기는 오류를 해결하기 위해서 new_circle에 기록하고, 마지막에 circle에 new_circle을 복사해줌
    new_circle=[arr[:] for arr in circle]
    for i in range(1,n+1):
        # 0이 아닌 값을 하나라도 가지고 있으면
        not_zero=[x for x in circle[i] if x!=0]
        if not_zero:
            isZero=True
            for j in range(1,m+1):
                if circle[i][j]!=0:
                    sumCircle+=circle[i][j]
                    numCircle+=1
                    for di in directions:
                        dy=i+di[0]
                        dx=j+di[1]
                        if 1<=dy<=n and 1<=dx<=m:
                            # 범위 안에 해당하면
                            if circle[dy][dx]==circle[i][j]:
                                isExist=True
                                new_circle[dy][dx]=0
                                new_circle[i][j]=0
                        else:
                            # 범위 밖이면서 dx의 경로가 벗어난 경우
                            if 1<=dy<=n and (dx<=0 or dx>m):
                                if dx<=0:
                                    dx=m
                                elif dx>m:
                                    dx=1
                                if circle[dy][dx] == circle[i][j]:
                                    isExist = True
                                    new_circle[dy][dx] = 0
                                    new_circle[i][j]=0
    if isExist==True:
        circle=[arr[:] for arr in new_circle]

    # 원판에 수가 존재하면서, 원판에 인접하면서 같은 수가 없다면
    if isExist == False and isZero==True:
        avg = sumCircle / numCircle
        for i in range(1,n+1):
            for j in range(1,m+1):
                if circle[i][j]>0:
                    if circle[i][j] > avg:
                        circle[i][j] -= 1
                    elif circle[i][j] < avg:
                        circle[i][j] += 1

for x,d,k in command:
    rotate(x,d,k)
    find_adjacent()

ans=0
for i in range(1, n+1):
    for j in range(1, m+1):
        ans+=circle[i][j]

print(ans)














