# n, m : 지도의 크기(n*m)
# x, y : 주사위를 놓은 곳의 좌표
# k : 명령의 개수

#수정요망
import sys
n,m,x,y,k=map(int, sys.stdin.readline().split(' '))

jido=[]
for i in range(n):
  tmp=map(int, sys.stdin.readline().split(' '))
  jido.append(list(tmp))

command=list(map(int, sys.stdin.readline().split(' ')))
# 각 방향별로 지도의 인덱스가 어떻게 변하는지 파악해야 함
# 초기 주사위 인덱스 및 적힌 수
# [북,남,서,동,앞,뒤]
# 남쪽으로 이동할 경우 -> [뒤,앞,서,동,북,남]
# 북쪽으로 이동할 경우 -> [앞,위,서,동,남,북]
# 서쪽으로 이동할 경우 -> [동,서,북,남,앞,뒤]
# 동쪽으로 이동할 경우 -> [서,동,남,북,앞,뒤]
dice=[(6,0),(1,0),(4,0),(3,0),(5,0),(2,0)]
#남 북 동 서
dix=[0,0,1,-1]
diy=[1,-1,0,0]
dx,dy=x,y
for comm in command:
  #동쪽으로 이동
  if comm==1:
    # 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.
    if 0<=(dx+dix[2])<m and 0<=(dy+diy[2])<n:
      # 좌표이동
      dx=dx+dix[2]
      dy=dy+diy[2]
      #주사위 동쪽으로 이동
      copydice=dice.copy()
      dice[0]=copydice[2]
      dice[1]=copydice[3]
      dice[2]=copydice[1]
      dice[3]=copydice[0]
      #이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
      if jido[dy][dx]==0:
        jido[dy][dx]=dice[1][1]
      #0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
      else:
        dice[1]=(dice[1][0],jido[dy][dx])
        jido[dy][dx]=0
      print(dice[0][1])
  #서쪽으로 이동
  elif comm==2:
    if 0<=(dx+dix[3])<m and 0<=(dy+diy[3])<n:
      dx=dx+dix[3]
      dy=dy+diy[3]
      #주사위 서쪽으로 이동
      copydice=dice.copy()
      dice[0]=copydice[3]
      dice[1]=copydice[2]
      dice[2]=copydice[0]
      dice[3]=copydice[1]
      #이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
      if jido[dy][dx]==0:
        jido[dy][dx]=dice[1][1]
      #0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
      else:
        dice[1]=(dice[1][0],jido[dy][dx])
        jido[dy][dx]=0
      print(dice[0][1])
  #북쪽으로 이동
  elif comm==3:
    if 0<=(dx+dix[1])<m and 0<=(dy+diy[1])<n:
      dx=dx+dix[1]
      dy=dy+diy[1]
      #주사위 북쪽으로 이동
      copydice=dice.copy()
      dice[0]=copydice[4]
      dice[1]=copydice[5]
      dice[4]=copydice[1]
      dice[5]=copydice[0]
      #이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
      if jido[dy][dx]==0:
        jido[dy][dx]=dice[1][1]
      #0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
      else:
        dice[1]=(dice[1][0],jido[dy][dx])
        jido[dy][dx]=0
      print(dice[0][1])
  #남쪽으로 이동
  elif comm==4:
    if 0<=(dx+dix[0])<m and 0<=(dy+diy[0])<n:
      dx=dx+dix[0]
      dy=dy+diy[0]
      #주사위 남쪽으로 이동
      copydice=dice.copy()
      dice[0]=copydice[5]
      dice[1]=copydice[4]
      dice[4]=copydice[0]
      dice[5]=copydice[1]
      #이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
      if jido[dy][dx]==0:
        jido[dy][dx]=dice[1][1]
      #0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
      else:
        dice[1]=(dice[1][0],jido[dy][dx])
        jido[dy][dx]=0
      print(dice[0][1])
        

