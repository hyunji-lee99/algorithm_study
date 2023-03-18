# 구현?


n,k=map(int, input().split(' '))
belts=list(map(int, input().split(' '))) # 내구도 배열
robot=[] #robot 위치 저장 배열
belts.insert(0,-1) #1-2*n 인덱스를 가지기 위한 더미 데이터 추가
is_robot=[False for _ in range(len(belts))]

def rotate():
    # 컨베이어 벨트 및 로봇 회전
    global belts, is_robot, robot
    # 컨베이어 벨트 회전
    p=belts.pop()
    belts.insert(1,p)
    # 로봇 회전
    new_robot=[]
    is_robot=[False for _ in range(len(belts))]
    for index in robot:
        next_index=index+1
        # 다음 칸이 n이하인 경우 새로운 로봇 인덱스 배열에 추가 (n 이상일 경우 내린 것으로 간주함)
        if next_index<n:
            new_robot.append(next_index)
            is_robot[next_index]=True
    robot=new_robot

def move_robot():
    # 로봇의 이동
    global robot, is_robot, belts
    new_robot=[]
    for index in robot:
        next_index=index+1
        # 이동이 불가능한 경우(다음 인덱스에 로봇이 이미 존재하거나, 내구도가 1 미만인 경우)
        if is_robot[next_index] or belts[next_index]<1:
            new_robot.append(index)
        # 이동이 가능한 경우
        else:
            # 다음 위치의 내구도를 1 감소시키고, 현재 위치에 로봇이 존재하지 않게 됨.
            belts[next_index]-=1
            is_robot[index]=False
            # 다음 위치가 n은 아닌지 파악
            if next_index<n:
                new_robot.append(next_index)
                is_robot[next_index]=True
    robot=new_robot

def insert_robot():
    # 올리는 위치 칸의 내구도가 0이 아니면 로봇을 올림
    global is_robot, robot, belts
    if belts[1]>=1:
        # 첫번째에 로봇이 존재하는 것을 기록
        is_robot[1]=True
        # 로봇의 새로운 위치 추가
        robot.append(1)
        # 첫번째 벨트의 내구도 1 감소
        belts[1]-=1

def is_finish():
    # 종료조건 확인(내구도가 0인 벨트가 k개 이상이 되면 True 반환)
    global k
    return belts.count(0)>=k

step=0
while not is_finish():
    step+=1
    rotate()
    move_robot()
    insert_robot()

print(step)
