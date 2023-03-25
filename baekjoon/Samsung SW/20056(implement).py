# python3 -> 시간초과, pypy3 -> 통과
# 시간을 줄이도록 코드 효율성 다시 생각해보기!

n,m,k=map(int, input().split(' '))

ball=[]
ballmap=[[[] for _ in range(n+1)] for _ in range(n+1)]

#m개 만큼 파이어볼 정보 받아서, 위치시킴
for i in range(m):
    r,c,m,s,d=map(int, input().split(' '))
    ball.append((r,c,m,s,d))

#파이어볼 이동
def move_fireball():
    global ball, ballmap
    # y x
    directions=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    # 갱신용 파이어볼 배열
    new_ball=[]
    while ball:
        r,c,m,s,d=ball.pop(0)
        ballmap[r][c].pop(0)
        dy=r+directions[d][0]*s
        dx=c+directions[d][1]*s
        if 1<=dy<=n and 1<=dx<=n:
            new_ball.append((dy,dx,m,s,d))
            ballmap[dy][dx].append((m,s,d))
        else:
            # y값이 범위를 벗어나는 경우
            if dy<=0:
                while dy<=0:
                    dy+=n
            elif dy>n:
                while dy>n:
                    dy-=n
            # x값이 범위를 벗어나는 경우
            if dx<=0:
                while dx<=0:
                    dx+=n
            elif dx>n:
                while dx>n:
                    dx-=n
            new_ball.append((dy,dx,m,s,d))
            ballmap[dy][dx].append((m, s, d))
    ball=new_ball

def write_ball():
    global ballmap
    for r,c,m,s,d in ball:
        ballmap[r][c].append((m,s,d))

# 한 칸에 두 개 이상 볼이 있는 경우 볼 합치기
def sum_and_split_ball():
    global ball, ballmap
    for i in range(1,n+1):
        for j in range(1,n+1):
            # 해당 위치가 2개 이상의 볼을 가지고 있을 때
            if len(ballmap[i][j])>1:
                msum=0
                ssum=0
                # 방향 다 더해서 짝수면 홀수/짝수만 존재하는 것 -> 짝짝홀홀 이어도 짝수가 나올 수 있음 하나하나 확인하는 방향으로 수정
                isOdd=0
                isEven=0
                for b in ballmap[i][j]:
                    msum+=b[0]
                    ssum+=b[1]
                    if b[2]%2==0:
                        isEven+=1
                    else:
                        isOdd+=1
                cm=msum//5
                cs=ssum//len(ballmap[i][j])
                # 기존 볼은 모두 삭제
                ballmap[i][j].clear()
                # ball 배열에서도 해당 위치 볼 모두 삭제(x,y값 중 하나라도 i,j가 아니면 삭제하면 안되는데, or대신 and로 작성해둬서 오류 발생했음)
                ball=[x for x in ball if x[0]!=i or x[1]!=j]
                if cm>0:
                    if isEven==len(ballmap[i][j]) or isOdd==len(ballmap[i][j]):
                        ballmap[i][j].append((cm, cs, 0))
                        ballmap[i][j].append((cm, cs, 2))
                        ballmap[i][j].append((cm, cs, 4))
                        ballmap[i][j].append((cm, cs, 6))
                        ball.append((i, j, cm, cs, 0))
                        ball.append((i, j, cm, cs, 2))
                        ball.append((i, j, cm, cs, 4))
                        ball.append((i, j, cm, cs, 6))

                    else:
                        ballmap[i][j].append((cm, cs, 1))
                        ballmap[i][j].append((cm, cs, 3))
                        ballmap[i][j].append((cm, cs, 5))
                        ballmap[i][j].append((cm, cs, 7))
                        ball.append((i, j, cm, cs, 1))
                        ball.append((i, j, cm, cs, 3))
                        ball.append((i, j, cm, cs, 5))
                        ball.append((i, j, cm, cs, 7))


cnt=1
# 초기 파이어볼 기록
write_ball()
while cnt<=k:
    cnt+=1
    # 파이어볼 이동
    move_fireball()
    # 볼 합치고 나누기
    sum_and_split_ball()

# 남은 볼의 질량 계산하기
ans=0
for r,c,m,s,d in ball:
    ans+=m

print(ans)








