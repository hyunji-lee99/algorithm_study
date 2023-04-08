n=int(input())
A=[list(map(int, input().split(' '))) for _ in range(n)]

# 가운데 시작
now=[n//2, n//2]

# 비율 저장
left=[(-2,0,0.02),(-1,0,0.07),(-1,-1,0.1),(-1,1,0.01),(0,-2,0.05),(1,-1,0.1),(1,0,0.07),(1,1,0.01),(2,0,0.02),(0,-1,0)]
right=[(y,-x,z) for y,x,z in left]
up=[(x,y,z) for y,x,z in left]
# down 좌표 설정 실수로 계속 틀렸음
down=[(-x,y,z) for y,x,z in left]

ans=0
def move_sand(cnt,dy,dx,rate):
    global ans
    for i in range(cnt):
        # cnt만큼 (dy,dx) 방향으로 이동
        now[0]+=dy
        now[1]+=dx
        # 토네이도 소멸되는 경우 끝
        if now[0]<0 or now[1]<0:
            break
        # 현재 칸의 모래 양
        now_sand=A[now[0]][now[1]]
        # 이동하는 방향대로 비율별로 흩어짐
        # 비율칸에 안착하거나, 바깥으로 나가는 모래의 양
        spread=0
        for y,x,r in rate:
            ny=now[0]+y
            nx=now[1]+x
            if r==0:
                sand=now_sand-spread
            else:
                sand=int(now_sand*r)

            if 0<=ny<n and 0<=nx<n:
                # 해당 칸에 모래 추가
                A[ny][nx]+=sand
            else:
                # 바깥으로 나가는 경우 ans에 추가
                ans+=sand
            # 비율 계산 총량
            spread+=sand
        # 남은 모래 소멸
        A[now[0]][now[1]]=0


# 홀수일 때, 서남
# 짝수일 때, 동북
for i in range(1,n+1):
    if i%2==0:
        # 동
        move_sand(i,0,1,right)
        # 북
        move_sand(i,-1,0,up)
    else:
        # 서
        move_sand(i, 0,-1,left)
        # 남
        move_sand(i, 1,0,down)

print(ans)