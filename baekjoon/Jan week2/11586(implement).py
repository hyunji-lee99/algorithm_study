# 거울의 심리상태 1이면, 있는 그대로
# 2이면, 좌우반전
# 3이면 상하반전
import sys
size=int(sys.stdin.readline())

jiyoung=[]
for i in range(size):
    tmp=list(sys.stdin.readline().strip())
    jiyoung.append(tmp)

feel=int(sys.stdin.readline())

#있는 그대로 출력
if feel==1:
    for i in range(size):
        for j in range(size):
            print(jiyoung[i][j],end='')
        print('')
#좌우반전 출력
elif feel==2:
    for i in range(size):
        for j in range(size-1,-1,-1):
            print(jiyoung[i][j],end='')
        print('')
#상하반전 출력
elif feel==3:
    for i in range(size-1,-1,-1):
        for j in range(size):
            print(jiyoung[i][j],end='')
        print('')
