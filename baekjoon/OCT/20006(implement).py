import sys

p, m = map(int, sys.stdin.readline().split(' '))

# 첫번째 플레이어의 방 추가
firstl, firstn=sys.stdin.readline().strip().split(' ')
rooms=[]
rooms.append([(int(firstl), firstn)])
for _ in range(p-1):
    level, nickname = sys.stdin.readline().strip().split(' ')
    level=int(level)
    # 들어갈 수 있는 방이 존재하는 경우
    # 1) 방의 인원이 m보다 작고, 첫번째 입장한 플레이어의 레벨과의 차이가 -10~+10이라면
    for room_no in range(len(rooms)):
        room_level=rooms[room_no][0][0]
        room_user=len(rooms[room_no])
        if room_user<m and room_level-10<=level and level<=room_level+10:
            rooms[room_no].append((level, nickname))
            break
    # 기존 방 중에 들어갈 수 있는 방이 없다면
    else:
        rooms.append([(level, nickname)])

for room in rooms:
    if len(room)==m:
        print("Started!")
        room.sort(key=lambda x:x[1])
        for player in room:
            print(player[0], player[1])
    else:
        print("Waiting!")
        room.sort(key=lambda x: x[1])
        for player in room:
            print(player[0], player[1])
