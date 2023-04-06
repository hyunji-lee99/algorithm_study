N,Q=map(int, input().split(' '))
ice=[list(map(int, input().split(' '))) for _ in range(pow(2,N))]
L=list(map(int, input().split(' ')))
width=pow(2,N)
def split_and_rotate(level):
    global ice, width
    # 2^level*2^level로 격자를 나눔
    l=pow(2,level)
    # 2차원 배열 split 하는 법
    # 시계방향으로 90도 회전 -> 전치행렬 한 뒤에, 각 행별로 reverse
    for i in range(0,width,l):
        for j in range(0,width,l):
            split2l = list(zip(*([ice[i+x][j:j+l] for x in range(l)])))
            cw = []
            for s in split2l:
                cw.append(list(reversed(s)))
            for v in range(l):
                ice[i+v][j:j+l]=cw.pop(0)[:]

# 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.
def minus_ice():
    global ice, width
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    melting_ice=[]
    for i in range(width):
        for j in range(width):
            if ice[i][j]==0:
                continue
            isice=0
            for di in directions:
                dy=i+di[0]
                dx=j+di[1]
                if 0<=dy<width and 0<=dx<width and ice[dy][dx]>0:
                    isice+=1
            if isice < 3:
                # 각 단계별로 탐색하면서 녹여주는 것이 아니라, 저장해놓고 한꺼번에 녹여야 제대로 된 계산값이 나옴
                melting_ice.append((i,j))

    for y,x in melting_ice:
        ice[y][x]-=1




for level in L:
    split_and_rotate(level)
    minus_ice()

# 남아있는 얼음의 합
ans_sum=0
for i in ice:
    ans_sum+=sum(i)

print(ans_sum)

# 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
# 얼음이 있는 칸이 얼음이 있는 칸과 인접해 있으면, 두 칸을 연결되어 있다고 한다. 덩어리는 연결된 칸의 집합이다.
def bfs(y,x):
    global ice, width, visited
    queue=[]
    queue.append((y,x))
    directions=[(0,1),(0,-1),(-1,0),(1,0)]
    size=0
    while queue:
        y,x=queue.pop(0)
        size+=1
        for di in directions:
            dy=y+di[0]
            dx=x+di[1]
            if 0<=dy<width and 0<=dx<width and visited[dy][dx]==0 and ice[dy][dx]>0:
                queue.append((dy,dx))
                visited[dy][dx]=1

    return size

visited=[[0]*width for _ in range(width)]
maxvalue=0
for i in range(width):
    for j in range(width):
        if ice[i][j]>0 and visited[i][j]==0:
            visited[i][j]=1
            maxvalue=max(maxvalue, bfs(i,j))

print(maxvalue)



