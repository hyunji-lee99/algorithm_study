# 틀렸음
m,s=map(int, input().split(' '))

# x,y,d
fish=[list(map(int, input().split(' '))) for _ in range(m)]
# dummy (행렬상 좌표 주의)
directions=[(),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

# 상어 위치
sx, sy=map(int, input().split(' '))

# 격자 칸의 상황(dummy 포함)
# 냄새 -> 2
area=[[0]*5 for _ in range(5)]

# 물고기 냄새를 남길 좌표 저장
delete_fish = []

def move_fish():
    global fish, area

    new_fish=[]
    while fish:
        x,y,d=fish.pop(0)
        # d에서 0까지 탐색(반시계 회전 인 것 주의!)
        for i in range(d,0,-1):
            dx=x+directions[i][0]
            dy=y+directions[i][1]
            # 격자 범위 안에 해당하면서 상어가 존재하거나 물고기 냄새가 존재하는 경우가 아니면 이동 가능
            if 1<=dx<=4 and 1<=dy<=4 and area[dx][dy]==0 and (dx!=sx or dy!=sy):
                new_fish.append([dx,dy,i])
                break
       # 위 for문에서 가능한 칸이 없을 경우, 끝에서 d까지 인덱스 탐색
        else:
            for i in range(8,d,-1):
                dx = x + directions[i][0]
                dy = y + directions[i][1]
                if 1 <= dx <= 4 and 1 <= dy <= 4 and area[dx][dy] == 0:
                    new_fish.append([dx, dy, i])
                    break
            # 모두 해당하지 않으면 기존 위치와 방향 다시 넣어줌
            else:
                new_fish.append([x,y,d])
    # fish 배열 update
    fish=[arr[:] for arr in new_fish]
    # 위치별 물고기 수 저장
    numberoffish = [[0] * 5 for _ in range(5)]
    for x,y,d in fish:
        numberoffish[x][y]+=1

    return numberoffish



def move_shark():
    global area, fish, nf, sy, sx, step, delete_fish
    # 인접한 상하좌우 칸으로 이동
    # 상 좌 하 우(x,y) 행 열로 생각
    direction=[(),(-1,0),(0,-1),(1,0),(0,1)]
    fishmax=-1e9
    dictmin=1e9
    # 상어가 이동할 최종 좌표
    change_x=sx
    change_y=sy
    # 3중 for문으로 각 단게를 거치면서 총 물고기 수를 파악하고, 사전순도 체크
    for one in range(1,5):
        for two in range(1,5):
            for three in range(1,5):
                new_x=sx
                new_y=sy
                numfish=0
                move_dir=[one, two, three]
                visited=[[0]*5 for _ in range(5)]
                for m in move_dir:
                    new_x=new_x+direction[m][0]
                    new_y=new_y+direction[m][1]
                    if 1<=new_x<=4 and 1<=new_y<=4:
                        # 이동하는 칸에 물고기가 존재하면
                        if nf[new_x][new_y]>0 and visited[new_x][new_y]==0:
                            # 먹은 물고기 수 더해주고
                            numfish+=nf[new_x][new_y]
                            # 방문 표시
                            visited[new_x][new_y] = 1
                    else:
                        # 범위을 벗어나면 해당 방법은 불가능한 것
                        break
                # for문을 도는 동안 break되지 않으면? -> 가능한 경로라는 뜻 -> 최대 물고기 값인지 확인
                else:
                    numdict = int(str(one) + str(two) + str(three))
                    if fishmax<numfish:
                        fishmax=numfish
                        dictmin=numdict
                        change_x=new_x
                        change_y=new_y
                    elif fishmax==numfish:
                        if dictmin>numdict:
                            dictmin=numdict
                            change_y=new_y
                            change_x=new_x
    # 최종적으로 정해진 dictmin으로 delete fish 저장
    t_sy=sy
    t_sx=sx
    for n in list(str(dictmin)):
        t_sx+=direction[int(n)][0]
        t_sy+=direction[int(n)][1]
        if nf[t_sx][t_sy]>0:
            delete_fish.append((t_sx,t_sy, step))
    # 상어 냄새 남기기
    area[sx][sy]=2
    # 상어 좌표 업데이트
    sy=change_y
    sx=change_x


    # delete_fish에 저장된 대로 해당 칸에 물고기 제거하고 냄새 남김
    for x,y,s in delete_fish:
        if s>step:
            break
        elif s==step:
            area[x][y]=2
        # 해당 칸 물고기 제거
        delelte_idx=[]
        for idx in range(len(fish)):
            if fish[idx][0]==x and fish[idx][1]==y:
                delelte_idx.append(idx)
        fish=[fish[i] for i in range(len(fish)) if i not in delelte_idx]


def delete_smell():
    global delete_fish, area, step
    for x,y,s in delete_fish:
        if s>(step-2):
            break
        elif s==(step-2):
            area[x][y]=0





step=1
while step<=s:
    # 상어가 복제 마법을 걸어둠
    copy_fish=[arr[:] for arr in fish]
    # 물고기가 한 칸씩 이동하고, 각 위치별로 물고기의 수를 나타내는 이차원 배열 nf를 리턴
    nf=move_fish()
    # 상어가 연속해서 3칸을 이동함
    move_shark()
    # 두 번 전 연습에서 남긴 냄새는 삭제
    delete_smell()
    # 복제 마법 완료
    fish+=copy_fish
    step+=1

# 격자에 존재하는 물고기의 수
print(len(fish))


