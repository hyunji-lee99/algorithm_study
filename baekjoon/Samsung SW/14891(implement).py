# 구현?

# 각 번호별로 톱니바퀴 입력받음
# 리스트로 처리히는 것이 구현이 편함
rot=[]
for i in range(4):
    tmp=list(map(int, list(input())))
    rot.append(tmp)

# 회전 명령의 횟수
n=int(input())

def rotate(num, dir):
    if dir==1:
        # typeError:can only concatenate list to list
        #rot[number-1]=rot[number-1][7]+rot[number-1][0:7]
        tmprot=[]
        tmprot.append(rot[num][7])
        tmprot=tmprot+rot[num][0:7]
        rot[num]=tmprot
    elif dir==-1:
        #rot[number-1]=rot[number-1][1:8]+rot[number-1][0]
        tmprot=rot[num][1:8]
        tmprot.append(rot[num][0])
        rot[num]=tmprot

for i in range(n):
    # direction이 1이면 시계방향
    # direction이 -1이면 반시계방향
    number, direction=map(int, input().split(' '))
    idx=number-1
    # bfs형식으로 해본다면?
    visited=[0]*4
    # 라이브러리없이 구현해야 하니까 deque 사용 X
    queue=[]
    queue.append((idx,direction))
    requireRotate=[]
    while queue:
        cur,dir=queue.pop(0)
        visited[cur]=1
        requireRotate.append((cur,dir))
        for i in (cur-1,cur+1):
            # 방문한 적 없을 경우
            if 0<=i<4 and visited[i]==0:
                # 왼쪽인 경우
                if i==cur-1:
                    # 맞닿은 부분이 서로 다른 극일 경우
                    if rot[i][2]!=rot[cur][6]:
                        if dir==-1:
                            queue.append((i,1))
                        elif dir==1:
                            queue.append((i,-1))
                elif i==cur+1:
                    if rot[i][6]!=rot[cur][2]:
                        if dir==-1:
                            queue.append((i,1))
                        elif dir==1:
                            queue.append((i,-1))
    for idx, dir in requireRotate:
        rotate(idx, dir)

score=0
# 2승 형태로 바꾸는 것도 좋을듯(1,2,4,8 형식으로 점수가 추가되니까)
if rot[0][0]==1:
    score+=1
if rot[1][0]==1:
    score+=2
if rot[2][0]==1:
    score+=4
if rot[3][0]==1:
    score+=8

print(score)