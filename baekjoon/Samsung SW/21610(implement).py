
n,m=map(int, input().split(' '))

water=[]
for i in range(n):
    tmp=list(map(int, input().split(' ')))
    tmp.insert(0,-1) #dummy
    water.append(tmp)

water.insert(0,[-1]*(n+1)) #dummy
clouds=[(n,1),(n,2),(n-1,1),(n-1,2)]
# dummy, 좌, 상좌, 상, 상우, 우, 하우, 하, 하좌 (y,x)
directions=[(0,0),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
def move_cloud(d,s):
    # 구름 이동
    global clouds, directions
    new_clouds=[]
    for cloud in clouds:
        next_dy=cloud[0]+directions[d][0]*s
        next_dx=cloud[1]+directions[d][1]*s
        # 범위를 벗어나지 않는 경우
        if 1<=next_dy<=n and 1<=next_dx<=n:
            new_clouds.append((next_dy,next_dx))
        # 범위를 벗어나는 경우
        else:
            # x측 범위 벗어나는 경우 탐색
            if next_dx<=0:
                while next_dx<=0:
                    tmp=n+next_dx
                    next_dx=tmp
            elif next_dx>n:
                while next_dx>n:
                    tmp=next_dx-n
                    next_dx=tmp
            # y축 범위 벗어나는 경우 탐색
            if next_dy<=0:
                while next_dy<=0:
                    tmp=n+next_dy
                    next_dy=tmp
            elif next_dy>n:
                while next_dy>n:
                    tmp=next_dy-n
                    next_dy=tmp
            new_clouds.append((next_dy,next_dx))

    #cloud update
    clouds=new_clouds

def add_water():
    global clouds, water, addedbucket
    for cloud in clouds:
        water[cloud[0]][cloud[1]]+=1
        # 물이 증가된 칸 저장
        addedbucket.append((cloud[0],cloud[1]))

def watercopybug():
    global clouds, water
    for bucket in addedbucket:
        # 대각선 방향은 direction에서 2,4,6,8
        # 주변에 물이 들어있는 바구니 수 체크
        check = 0
        for i in range(2, 9, 2):
            next_dy=bucket[0]+directions[i][0]
            next_dx=bucket[1]+directions[i][1]
            # 물복사는 이동과 달리 경계 안에 있는 경우에만 발생 가능
            if 1<=next_dx<=n and 1<=next_dy<=n and water[next_dy][next_dx]>0:
                check+=1
        water[bucket[0]][bucket[1]]+=check

def add_cloud():
    global water, remove_cloud, clouds
    # 물의 양이 2 이상인 바구니 위치 탐색
    for i in range(1,n+1):
        for j in range(1,n+1):
            # 물의 양이 2 이상이면서 제거된 구름의 위치가 아닌 경우
            if water[i][j]>=2 and (i,j) not in remove_cloud:
                water[i][j] -= 2
                clouds.append((i, j))


for i in range(m):
    d,s=map(int, input().split(' '))
    remove_cloud = []
    addedbucket = []
    # 모든 구름이 di 방향으로 si칸 이동한다.
    move_cloud(d,s)
    # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    add_water()
    # 구름이 사라진 칸 저장 모두 저장하고, 구름 모두 사라진다
    remove_cloud=clouds.copy()
    clouds.clear()
    # 물복사버그
    watercopybug()
    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고 물의 양이 2 줄어듬. (단, 구름이 사라졌던 칸은 아니어야 함)
    add_cloud()

sumwater=0
for i in range(1, n+1):
    for j in range(1,n+1):
        sumwater+=water[i][j]

print(sumwater)

