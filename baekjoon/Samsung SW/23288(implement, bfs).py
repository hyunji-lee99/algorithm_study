n,m,k=map(int, input().split(' '))
# dummy
area=[[0]*(m+1)]+[[0]+list(map(int, input().split(' '))) for _ in range(n)]

# 상, 동, 서, 남, 북, 하
# dice init
dice=[1, 3, 4, 5, 2, 6]

def move_east(dice):
    new_dice=dice.copy()
    new_dice[0]=dice[2]
    new_dice[1]=dice[0]
    new_dice[2]=dice[5]
    new_dice[5]=dice[1]
    return new_dice

def move_west(dice):
    new_dice=dice.copy()
    new_dice[0]=dice[1]
    new_dice[1] = dice[5]
    new_dice[2] = dice[0]
    new_dice[5] = dice[2]
    return new_dice

def move_north(dice):
    new_dice = dice.copy()
    new_dice[0] = dice[3]
    new_dice[3] = dice[5]
    new_dice[4] = dice[0]
    new_dice[5] = dice[4]
    return new_dice

def move_south(dice):
    new_dice = dice.copy()
    new_dice[0] = dice[4]
    new_dice[3] = dice[0]
    new_dice[4] = dice[5]
    new_dice[5] = dice[3]
    return new_dice

move_dice=[move_east, move_west, move_south, move_north]
# 동 서 남 북(y x)
direcionts=[(0,1),(0,-1),(1,0),(-1,0)]
cur_dir=0
cur_location=[1,1]

def move():
    global move_dice, cur_dir, dice
    dy=cur_location[0]+direcionts[cur_dir][0]
    dx=cur_location[1]+direcionts[cur_dir][1]
    # 이동할 수 있으면
    if 1<=dy<=n and 1<=dx<=m:
        cur_location[0]=dy
        cur_location[1]=dx
        dice=move_dice[cur_dir](dice)
    # 이동할 수 없으면 반대 방향으로 이동
    else:
        if cur_dir==0:
            cur_dir=1
        elif cur_dir==1:
            cur_dir=0
        elif cur_dir==2:
            cur_dir=3
        elif cur_dir==3:
            cur_dir=2
        cur_location[0] = cur_location[0] + direcionts[cur_dir][0]
        cur_location[1] = cur_location[1] + direcionts[cur_dir][1]
        dice = move_dice[cur_dir](dice)


def scoreXY():
    global direcionts, cur_location, n,m, area
    B=area[cur_location[0]][cur_location[1]]
    C=0
    queue=[(cur_location[0],cur_location[1])]
    visited=[[0]*(m+1) for _ in range(n+1)]
    visited[cur_location[0]][cur_location[1]]=1
    while queue:
        y,x=queue.pop(0)
        C+=1
        for di in direcionts:
            dy=y+di[0]
            dx=x+di[1]
            if 1<=dy<=n and 1<=dx<=m and visited[dy][dx]==0 and area[dy][dx]==B:
                queue.append((dy,dx))
                visited[dy][dx]=1
    return B*C

def change_direction():
    global cur_dir, cur_location, area, dice
    y=cur_location[0]
    x=cur_location[1]
    B=area[y][x]
    A=dice[5]
    if A>B:
        # 시계방향으로 회전
        if cur_dir==0:
            cur_dir=2
        elif cur_dir==1:
            cur_dir=3
        elif cur_dir==2:
            cur_dir=1
        elif cur_dir==3:
            cur_dir=0
    elif A<B:
        # 반시계방향으로 회전
        if cur_dir==0:
            cur_dir=3
        elif cur_dir==1:
            cur_dir=2
        elif cur_dir==2:
            cur_dir=0
        elif cur_dir==3:
            cur_dir=1


cnt=1
score=0
while cnt<=k:
    move()
    score+=scoreXY()
    change_direction()
    cnt+=1

print(score)


